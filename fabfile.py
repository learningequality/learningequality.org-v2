# import datetime
import os
import subprocess
from shlex import quote, split

from invoke import run as local
from invoke.exceptions import Exit
from invoke.tasks import task

# Process .env file
if os.path.exists(".env"):
    with open(".env", "r") as f:
        for line in f.readlines():
            if line.startswith("#"):
                continue
            var, value = line.strip().split("=", 1)
            os.environ.setdefault(var, value)

FRONTEND = os.getenv("FRONTEND", "docker")

PROJECT_DIR = "/app"

PRODUCTION_APP_INSTANCE = "learning_equality-production"
STAGING_APP_INSTANCE = "learning_equality-staging"
DEVELOPMENT_APP_INSTANCE = "learning_equality-dev"

LOCAL_MEDIA_FOLDER = "media"
LOCAL_IMAGES_FOLDER = "media/original_images"
LOCAL_DATABASE_NAME = PROJECT_NAME = "learning_equality"
LOCAL_DATABASE_USERNAME = "learning_equality"


############
# Production
############


def dexec(cmd, service="web"):
    return local(
        "docker-compose exec -T {} bash -c {}".format(quote(service), quote(cmd))
    )


def sudexec(cmd, service="web"):
    return local(
        "docker-compose exec --user=root -T {} bash -c {}".format(
            quote(service), quote(cmd)
        )
    )


@task
def build(c):
    """
    Build the development environment (call this first)
    """
    group = subprocess.check_output(["id", "-gn"], encoding="utf-8").strip()
    local("mkdir -p media database_dumps")
    local("chown -R $USER:{} media database_dumps".format(group))
    local("chmod -R 775 media database_dumps")
    if FRONTEND == "local":
        local("docker-compose up -d --build web")
    else:
        local("docker-compose up -d --build web frontend")
        dexec("npm ci", service="frontend")
    local("docker-compose stop")
    print("Project built: now run 'fab start'")


@task
def start(c):
    """
    Start the development environment
    """
    if FRONTEND == "local":
        local("docker-compose up -d web")
    else:
        local("docker-compose up -d web frontend")

    print("Use `fab sh` to enter the web container and run `djrun`")
    if FRONTEND != "local":
        print("Use `fab npm start` to run the front-end tooling")


@task
def stop(c):
    """
    Stop the development environment
    """
    local("docker-compose stop")


@task
def restart(c):
    """
    Restart the development environment
    """
    stop(c)
    start(c)


@task
def destroy(c):
    """
    Destroy development environment containers (database will lost!)
    """
    local("docker-compose down")


@task
def sh(c):
    """
    Run bash in the local web container
    """
    subprocess.run(["docker-compose", "exec", "web", "bash"])


@task
def sh_root(c):
    """
    Run bash as root in the local web container
    """
    subprocess.run(["docker-compose", "exec", "--user=root", "web", "bash"])


@task
def npm(c, command, daemonise=False):
    """
    Run npm in the frontend container E.G fab npm 'test'
    """
    exec_args = []
    if daemonise:
        exec_args.append("-d")
    subprocess.run(
        ["docker-compose", "exec"] + exec_args + ["frontend", "npm"] + split(command)
    )


@task
def psql(c):
    """
    Connect to the local postgres DB using psql
    """
    subprocess.run(
        [
            "docker-compose",
            "exec",
            "db",
            "psql",
            f"-d{LOCAL_DATABASE_NAME}",
            f"-U{LOCAL_DATABASE_USERNAME}",
        ]
    )


def delete_docker_database(c, local_database_name=LOCAL_DATABASE_NAME):
    dexec(
        "dropdb --if-exists --host db --username={project_name} {database_name}".format(
            project_name=PROJECT_NAME, database_name=LOCAL_DATABASE_NAME
        ),
        "db",
    )
    dexec(
        "createdb --host db --username={project_name} {database_name}".format(
            project_name=PROJECT_NAME, database_name=LOCAL_DATABASE_NAME
        ),
        "db",
    )


@task
def import_data(c, database_filename):
    """
    Import local data file to the db container.
    """
    # Copy the data file to the db container
    delete_docker_database(c)
    # Import the database file to the db container
    dexec(
        "pg_restore --clean --no-acl --if-exists --no-owner --host db \
            --username={project_name} -d {database_name} {database_filename}".format(
            project_name=PROJECT_NAME,
            database_name=LOCAL_DATABASE_NAME,
            database_filename=database_filename,
        ),
        service="db",
    )
    print(
        "Any superuser accounts you previously created locally will have been wiped and will need to be recreated."
    )


def delete_local_renditions(c, local_database_name=LOCAL_DATABASE_NAME):
    try:
        psql(c, "DELETE FROM images_rendition;")
    except Exception:
        pass

    try:
        psql(c, "DELETE FROM wagtailimages_rendition;")
    except Exception:
        pass


#########
# Production
#########

# add tasks needed for production here

#########
# Staging
#########

# add tasks needed for staging here

#############
# Development
#############


def delete_local_database(c, local_database_name=LOCAL_DATABASE_NAME):
    local(
        "dropdb --if-exists {database_name}".format(database_name=LOCAL_DATABASE_NAME)
    )


#######
# Utils
#######


def make_bold(msg):
    return "\033[1m{}\033[0m".format(msg)


@task
def dellar_snapshot(c, filename):
    """Snapshot the database, files will be stored in the db container"""
    dexec(
        "pg_dump -d {database_name} -U {database_username} > {filename}.psql".format(
            database_name=LOCAL_DATABASE_NAME,
            database_username=LOCAL_DATABASE_USERNAME,
            filename=filename,
        ),
        service="db",
    ),
    print("Database snapshot created")


@task
def dellar_restore(c, filename):
    """ Restore the database from a snapshot in the db container """
    delete_docker_database(c)

    dexec(
        "psql -U {database_username} -d {database_name} < {filename}.psql".format(
            database_name=LOCAL_DATABASE_NAME,
            database_username=LOCAL_DATABASE_USERNAME,
            filename=filename,
        ),
        service="db",
    ),
    print("Database restored.")


@task
def docker_coverage(c):
    return dexec(
        "coverage erase && coverage run manage.py test \
            --settings=learning_equality.settings.test && coverage report",
        service="web",
    )


@task
def run_test(c):
    """
    Run python tests in the web container
    """
    subprocess.call(
        [
            "docker-compose",
            "exec",
            "web",
            "python",
            "manage.py",
            "test",
            "--settings=learning_equality.settings.test",
            "--parallel",
        ]
    )

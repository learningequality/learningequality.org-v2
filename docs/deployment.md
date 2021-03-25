# Learning Equality Website — hosts and deployment

The VM comes preinstalled with Fabric, Heroku CLI and AWS CLI.

## Deployed environments

| Environment | Branch    | URL                                                    | Heroku                                 |
| ----------- | --------- | ------------------------------------------------------ | -------------------------------------- |
| Production  | `master`  | e.g. https://learning_equality.org                  | e.g. `learning_equality-production` |
| Staging     | `staging` | e.g. https://learning_equality.staging.torchbox.com | e.g. `learning_equality-staging`    |

## Login to Heroku

Please log in to Heroku before executing any commands for servers hosted there
using the `Heroku login -i` command. You have to do it both in the VM and your
host machine if you want to be able to use it in both places.

## Connect to the shell

To open the shell of the servers.

```bash
fab dev-shell
fab staging-shell
fab production-shell
```

## Scheduled tasks

When you set up a server you should make sure the following scheduled tasks are set.

- `django-admin publish_scheduled_pages` - every 10 minutes or more often. This is necessary to make publishing scheduled pages work.
- `django-admin clearsessions` - once a day (not necessary, but useful).
- `django-admin update_index` - once a day (not necessary, but useful to make sure the search index stays intact).

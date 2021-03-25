# Learning Equality Website — Data Protection

This page gives an overview of potentially-sensitive data stored or processed by the Learning Equality Website project.

### User accounts

What personally-identifying data is stored in a user’s account?

### Other

Describe other stored or processed data here, and steps made to ensure this is compliant with GDPR, e.g.

- visitor enquiries
- user emails, e.g. newsletter subscription requests
- customer or purchase details
- stored Wagtail FormPage submissions

## Data locations

### Logical location of data

Where is the GDPR-related data stored? Does this include any backups, or exports?

### Physical location of data

Our Heroku databases are stored in the EU region on AWS, as are all of the Heroku addons. The exception is database backups:

> "All backup files that are taken using Heroku PGBackups are stored in an encrypted S3 bucket in the US region."
> —https://devcenter.heroku.com/articles/heroku-postgres-production-tier-technical-characterization#data-encryption

This arrangement was originally compliant with GDPR ruling, based on a specific approval under the International Safe Harbor (sic) Privacy Principles: https://aws.amazon.com/blogs/security/customer-update-aws-and-eu-safe-harbor/. Safe Harbor is now defunct, was for a while superseded by the EU-US Privacy Shield, and that too is now declared invalid.

Heroku now has Standard Contractual Clauses whose use is still upheld by the ECJ, but the PDF link to those is unavailable at the time of writing this documentation:

> To see our GDPR, Salesforce Processor Binding Corporate Rules, and Standard Contractual Clauses visit our [Data Processing Addendum Website](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/data-processing-addendum.pdf).
> —https://devcenter.heroku.com/articles/gdpr

### Exports

All exports include the above data. The first steps when downloading a copy of the production database, or cloning it to staging, should be to delete all records in the user-submitted tables:

```bash
$ python manage.py shell_plus
>>> FormSubmission.objects.all().delete()
```

When copying the data to staging, decide whether to leave user accounts intact: delete them if users are members of the public, don't if they're client employees who will still want to access the staging site. If using the data locally, you should anonymise user accounts:

```bash
$ python manage.py shell_plus
>>> for user in User.objects.all():
...     user.first_name = "User"
...     user.last_name = user.id
...     user.email = f"user.{user.id}@example.com"
...     user.username = f"user.{user.id}"
...     user.save()
```

## Responding to GDPR requests

If a request is received to purge or report the stored data for a given user, what steps are needed?

- For user account data, delete the user from the Wagtail admin
- For form submissions, ask the client to handle requests as the first option. Failing that, search the submissions and delete if necessary using the Django shell.

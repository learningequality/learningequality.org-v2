# Learning Equality Website — Anonymising data

When pulling data from any hosted instance, take a cautious approach about whether you need full details of potentially personally-identifying, confidential or sensitive data.

General advice:

- pull data from staging rather than production servers, if this is good enough for your needs
- if it is necessary to pull data from production, e.g. for troubleshooting, consider whether anonymising personal data is possible and compatible with your needs
- if it is necessary to pull non-anonymised data from production, consider destroying this copy of the data as soon as you no longer need it

In more sensitive cases, consider a data protection policy to prevent access to production data except for authorised users.

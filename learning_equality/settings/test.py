from .base import *  # noqa

# #############
# General

# SECRET_KEY is required by Django to start.
SECRET_KEY = "fake_secret_key_to_run_tests"  # pragma: allowlist secret

# Silence RECAPTCHA
RECAPTCHA_PUBLIC_KEY = "dummy-key-value"
RECAPTCHA_PRIVATE_KEY = "dummy-key-value"  # pragma: allowlist secret

# Don't redirect to HTTPS in tests.
SECURE_SSL_REDIRECT = False

# #############
# Performance

# By default, Django uses a computationally difficult algorithm for passwords hashing.
# We don't need such a strong algorithm in tests, so use MD5
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

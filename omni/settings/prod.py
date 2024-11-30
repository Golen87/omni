""" Production Settings """

import os
from .dev import *

# Debug = False

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# Set Domain here
ALLOWED_HOSTS = ["localhost", "omni.espeon.dev"]
CSRF_TRUSTED_ORIGINS = ["https://omni.espeon.dev"]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "omni",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

# Logging
SERVER_EMAIL = "root@localhost"
ADMINS = (("root", "root@localhost"),)
"""
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "gunicorn": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": "/var/log/gunicorn.errors",
            "maxBytes": 1024 * 1024 * 100,  # 100 mb
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "gunicorn.errors": {
            "handlers": ["gunicorn"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
"""


# Security
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 3600
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
# SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = "DENY"

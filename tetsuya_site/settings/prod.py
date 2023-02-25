import os

from .base import *  # noqa: F401,F403

AWS_ACCESS_KEY_ID = os.environ.get("AWS_S3_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_S3_SECRET_ACCESS_KEY")

STATICFILES_STORAGE = "storages.backends.s3boto3.S3ManifestStaticStorage"
DEFAULT_FILE_STORAGE = "tetsuya_site.storage_backends.MediaStorage"

AWS_LOCATION = "static"

# JWT_AUTH_SECURE = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

AWS_S3_CUSTOM_DOMAIN = os.environ.get("AWS_S3_CUSTOM_DOMAIN")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_NAME"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}


# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "filters": {
#         "require_debug_false": {
#             "()": "django.utils.log.RequireDebugFalse",
#         },
#     },
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#         },
#         "mail_admins": {
#             "class": "django.utils.log.AdminEmailHandler",
#             "filters": ["require_debug_false"],
#             "level": "ERROR",
#         },
#         "null": {
#             "class": "logging.NullHandler",
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console"],
#             "propagate": True,
#         },
#         "django.request": {
#             "handlers": ["mail_admins"],
#             "propagate": False,
#         },
#         "django.security.DisallowedHost": {
#             "handlers": ["null"],
#             "propagate": False,
#         },
#     },
# }

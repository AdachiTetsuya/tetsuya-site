import os

from .base import *  # noqa: F401,F403
from .utils import strtobool

DEBUG = strtobool(os.getenv("DEBUG", "y"))

# コンソール上にユーザ登録確認メールを表示。ローカルで確認するため
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INTERNAL_IPS = ["127.0.0.1"]

# AWS_S3_CUSTOM_DOMAIN = "d1j0joz20lcidd.cloudfront.net"

# SQL の確認
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#         },
#     },
#     "loggers": {
#         "django.db.backends": {
#             "handlers": ["console"],
#             "level": "DEBUG",
#         },
#     },
# }

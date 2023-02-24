import os

from .base import *  # noqa: F401,F403
from .utils import strtobool

DEBUG = strtobool(os.getenv("DEBUG", "y"))

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

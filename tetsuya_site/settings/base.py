import os
from datetime import timedelta
from pathlib import Path

import dj_database_url

from .utils import strtobool

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "^7-2$6%6)kpa#cwba@zo=c@j+%xjppaldns)$nwu)#n4-6y_i)",
)

DEBUG = strtobool(os.getenv("DEBUG", "n"))

ALLOWED_HOSTS = [s.strip() for s in os.getenv("ALLOWED_HOSTS", "").split(",") if s]

# ALLOWED_HOSTS = ["52.199.38.147"]

CORS_ALLOWED_ORIGINS = [s.strip() for s in os.getenv("CORS_ALLOWED_ORIGINS", "").split(",") if s]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "chat_app",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "storages",
    "django_ses",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tetsuya_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "tetsuya_site.wsgi.application"

# Database

DATABASES = {
    "default": dj_database_url.config(default="sqlite:///db.sqlite3"),
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization

LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = "/static/"

# User-uploaded files

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email

EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")

# EMAIL_HOST = os.getenv("EMAIL_HOST", "")
# EMAIL_PORT = int(os.getenv("EMAIL_PORT", "25"))
# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
# EMAIL_USE_TLS = EMAIL_PORT == 578
# EMAIL_USE_SSL = EMAIL_PORT == 465

AWS_SES_REGION_NAME="us-east-1"
AWS_SES_REGION_ENDPOINT="email.us-east-1.amazonaws.com"
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "no-reply@example.com")
AWS_SES_ACCESS_KEY_ID=os.getenv("AWS_SES_ACCESS_KEY_ID")
AWS_SES_SECRET_ACCESS_KEY=os.getenv("AWS_SES_SECRET_ACCESS_KEY")

# Logging

SERVER_EMAIL = os.getenv("SERVER_EMAIL", DEFAULT_FROM_EMAIL)

ADMINS = list(
    zip(
        os.getenv("ADMIN_NAMES", "").split(","),
        os.getenv("ADMIN_EMAILS", "").split(","),
    )
)

AUTH_USER_MODEL = "chat_app.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

SITE_ID = 1


REST_AUTH = {
    "USE_JWT" : True,
    "JWT_AUTH_COOKIE" : "mysite-auth",
    "JWT_AUTH_REFRESH_COOKIE" : "mysite-refresh-token",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
}

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_ADAPTER = 'chat_app.adapter.AccountAdapter'

LOGOUT_ON_PASSWORD_CHANGE = False
OLD_PASSWORD_FIELD_ENABLED = True

DEFAULT_FILE_STORAGE = "tetsuya_site.storage_backends.MediaStorage"

AWS_S3_CUSTOM_DOMAIN = os.environ.get("AWS_S3_CUSTOM_DOMAIN")
AWS_STORAGE_BUCKET_NAME = "tetsuya-site-be-bucket"
AWS_CLOUDFRONT_KEY = os.environ.get("AWS_CLOUDFRONT_KEY", None).encode("ascii")
AWS_CLOUDFRONT_KEY_ID = os.environ.get("AWS_CLOUDFRONT_KEY_ID", None)

CORS_ALLOW_CREDENTIALS = True

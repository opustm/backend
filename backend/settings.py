"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "&)c@moy8m&hu%@e&7g-7qd&m2dacujlo$$cq3i(@dtv8#pof47"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "main.apps.MainConfig",
]

JWT_AUTH = {"JWT_RESPONSE_PAYLOAD_HANDLER": "backend.utils.my_jwt_response_handler"}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTH_USER_MODEL = "main.User"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
}


CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = (
    "http://localhost:3000",
    "https://opustm.herokuapp.com",
)

CSRF_TRUSTED_ORIGINS = ["localhost:3000", "opustm.herokuapp.com"]

CORS_ORIGIN_WHITELIST = ("localhost:3000",)


ROOT_URLCONF = "backend.urls"
# CORS_ALLOW_ALL_ORIGINS=True
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
staging = "postgres://jccljrzydpfygp:8d28f514694ad0f24698f04103e3888be266fbde875cd9a924e5a74c356eec15@ec2-54-158-222-248.compute-1.amazonaws.com:5432/d3ucugchgunj1h"
production = "postgres://dorwisqovqacjy:604b96b13eaf7f654eda750c48812d6f046f6e42874721a8e5163d31be490b09@ec2-52-2-82-109.compute-1.amazonaws.com:5432/daoainmikocqe6"
DATABASES = {}

STAGING_DATABASE = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": "d3ucugchgunj1h",
    "USER": "jccljrzydpfygp",
    "PASSWORD": "8d28f514694ad0f24698f04103e3888be266fbde875cd9a924e5a74c356eec15",
    "HOST": "ec2-54-158-222-248.compute-1.amazonaws.com",
    "PORT": "5432",
}

PRODUCTION_DATABASE = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": "daoainmikocqe6",
    "USER": "dorwisqovqacjy",
    "PASSWORD": "604b96b13eaf7f654eda750c48812d6f046f6e42874721a8e5163d31be490b09",
    "HOST": "ec2-52-2-82-109.compute-1.amazonaws.com",
    "PORT": "5432",
}

TEST_DATABASE = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
}

if "test" in sys.argv:
    DATABASES["default"] = TEST_DATABASE
else:
    DATABASES["default"] = STAGING_DATABASE

    DATABASES["default"] = dj_database_url.parse(production, conn_max_age=600)


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

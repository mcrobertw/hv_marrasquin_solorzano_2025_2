from pathlib import Path

import os

import dj_database_url

from dotenv import load_dotenv


# =====================

# CARGAR VARIABLES DE ENTORNO

# =====================

load_dotenv()


# =====================

# BASE

# =====================

BASE_DIR = Path(__file__).resolve().parent.parent


# =====================

# SEGURIDAD

# =====================

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")


DEBUG = os.getenv("DEBUG", "0") == "1"


ALLOWED_HOSTS = os.getenv(

    "ALLOWED_HOSTS",

    "localhost,127.0.0.1,hojadevida-bootcamp-romau-c4ayawcwaefqekge.centralus-01.azurewebsites.net"

).split(",")


CSRF_TRUSTED_ORIGINS = [

    f"https://{host.strip()}"

    for host in ALLOWED_HOSTS

    if host not in ["localhost", "127.0.0.1"]

]


# =====================

# APPS

# =====================

INSTALLED_APPS = [

    "django.contrib.admin",

    "django.contrib.auth",

    "django.contrib.contenttypes",

    "django.contrib.sessions",

    "django.contrib.messages",

    "django.contrib.staticfiles",


    "storages",          # SIEMPRE ACTIVO

    "cv",

]


# =====================

# MIDDLEWARE

# =====================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",


    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]


# =====================

# URLS / WSGI

# =====================

ROOT_URLCONF = "django_portfolio.urls"

WSGI_APPLICATION = "django_portfolio.wsgi.application"


# =====================

# TEMPLATES

# =====================

TEMPLATES = [

    {

        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [BASE_DIR / "templates"],

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


# =====================

# DATABASE

# =====================

DATABASE_URL = os.getenv("DATABASE_URL")


if DATABASE_URL:

    DATABASES = {

        "default": dj_database_url.parse(

            DATABASE_URL,

            conn_max_age=600,

            ssl_require=True,

        )

    }

else:

    DATABASES = {

        "default": {

            "ENGINE": "django.db.backends.sqlite3",

            "NAME": BASE_DIR / "db.sqlite3",

        }

    }


# =====================

# PASSWORD VALIDATION

# =====================

AUTH_PASSWORD_VALIDATORS = [

    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},

    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},

    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},

    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},

]


# =====================

# INTERNACIONALIZACIÓN

# =====================

LANGUAGE_CODE = "es-es"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# =====================

# STATIC FILES

# =====================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# =====================

# STORAGE (DJANGO ≥ 4.2)

# =====================

STORAGES = {

    "default": {

        "BACKEND": "storages.backends.azure_storage.AzureStorage",

    },

    "staticfiles": {

        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",

    },

}


# =====================

# AZURE BLOB STORAGE

# =====================

AZURE_ACCOUNT_NAME = os.getenv("AZURE_ACCOUNT_NAME")

AZURE_ACCOUNT_KEY = os.getenv("AZURE_ACCOUNT_KEY")

AZURE_CONTAINER = os.getenv("AZURE_CONTAINER", "media")


AZURE_OVERWRITE = False

AZURE_CUSTOM_DOMAIN = f"{AZURE_ACCOUNT_NAME}.blob.core.windows.net"


MEDIA_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{AZURE_CONTAINER}/"


# =====================

# DEFAULT

# =====================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
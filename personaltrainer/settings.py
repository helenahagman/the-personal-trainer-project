"""
Django settings for personaltrainer project.

Generated by 'django-admin startproject' using Django 3.2.20.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
if os.path.isfile('env.py'):
    import env

import dj_database_url

from decouple import config
from dotenv import load_dotenv

from pathlib import Path

import cloudinary
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if 'DEVELOPMENT' in os.environ and os.environ['DEVELOPMENT'].lower() == 'true':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [
    '8000-helenahagman-the-persona-6du395rfey.us2.codeanyapp.com',
    'ptproject.herokuapp.com',
    'ptproject-ec6a8ad157bf.herokuapp.com',
    'localhost',
    '8000-helenahagman-the-persona-9mdh98ciyo.us2.codeanyapp.com',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'ptproject',
    'ptproject.templatetags.custom_filters',
    'django_summernote',
    'cloudinary',
    'cloudinary_storage',
    'crispy_forms',
]

SITE_ID = 1

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_EMAIL_VERIFICATION = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'personaltrainer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

WSGI_APPLICATION = 'personaltrainer.wsgi.application'

database_url = os.environ.get("DATABASE_URL")

if database_url:
    # Parse the database URL using dj_database_url.config
    db_from_env = dj_database_url.config(default=database_url)

    # Update the OPTIONS to include the query parameters
    db_from_env['OPTIONS'] = {}
    if '?' in database_url:
        query_params = database_url.split('?')[1]
        db_from_env['OPTIONS']['sslmode'] = 'require'
        db_from_env['OPTIONS']['sslcompression'] = True
        db_from_env['OPTIONS']['sslcert'] = '/etc/ssl/certs/ca-certificates.crt'
        db_from_env['OPTIONS']['sslkey'] = '/etc/ssl/certs/ca-certificates.key'
        db_from_env['OPTIONS']['sslrootcert'] = '/etc/ssl/certs/ca-certificates.crt'
        db_from_env['OPTIONS']['ssl_cipher'] = 'HIGH:!aNULL:!MD5'

    DATABASES = {
        'default': db_from_env
    }
else:
    # If DATABASE_URL is not set, fallback to a default database configuration
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Load environment variables from .env file
CLOUD_NAME = os.getenv('CLOUD_NAME', 'default_value')
API_KEY = os.getenv('API_KEY', 'default_value')
API_SECRET = config('API_SECRET', 'default_value')

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': CLOUD_NAME,
    'API_KEY': API_KEY,
    'API_SECRET': API_SECRET,
}

# Cloudinary configuration
cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=CLOUDINARY_STORAGE['API_KEY'],
    api_secret=CLOUDINARY_STORAGE['API_SECRET']
)

# Default file storage for media files
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

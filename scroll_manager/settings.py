
# scroll_manager/settings.py

"""
Django settings for scroll_manager project.

"""

# Import standard libraries
import os
from pathlib import Path


# Import `env.py` if it exists for additional environment variables
# This is typically used in development environments
if os.path.isfile('env.py'):
    import env


# Import database URL handling library after environment variables are set up
import dj_database_url


# Cloudinary imports
import cloudinary
import cloudinary.uploader
import cloudinary.api


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret, don't 
# run with debug turned on in production!
# Get the secret key from the environment variable
SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-development-key')

# Raise an error if SECRET_KEY is not set for production
if SECRET_KEY == 'your-default-development-key' and os.getenv('DEVELOPMENT') is None:
    raise ValueError("No SECRET_KEY set for the Django application.")

# SECURITY WARNING: don't run with debug turned on in production! (Set to True for development)
# Set DEBUG based on environment
DEBUG = os.getenv('DEBUG', 'False') == 'True'  # True for dev, False for prod

ALLOWED_HOSTS = [
    '127.0.0.1',
    '.herokuapp.com',
    'scrollstack-af4b226be9f2.herokuapp.com/',
    '8000-jaqikal-scrollstack-5swovgh53o4.ws-eu110.gitpod.io',
    '.gitpod.io'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    # Optional -- requires install using `django-allauth[socialacocunt]`.
    'allauth.socialaccount',

    # user app
    'scroll_core',
    'scroll_home',

    # Other
    'crispy_forms',
    'crispy_bootstrap5',
    'cloudinary',
    'cloudinary_storage',
    'djrichtextfield']

SITE_ID = 1

# Amended from https://pypi.org/project/django-richtextfield/
DJRICHTEXTFIELD_CONFIG = {
    'js': ['//cdn.ckeditor.com/4.16.2/standard/ckeditor.js'],
    'init_template': 'djrichtextfield/init/ckeditor.js',
    'settings': {
        'toolbar': [
            ['Format', 'Bold', 'Italic', 'Underline'],
            ['Undo', 'Redo'],
            ['Link', 'Unlink'],
            ['NumberedList', 'BulletedList'],
            ['Source']
        ],
        'format_tags': 'p;h1;h2;h3;h4;h5;h6;pre;address;div',
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.locale.LocaleMiddleware',

]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'


ROOT_URLCONF = 'scroll_manager.urls'

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
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'scroll_core.context_processors.user_book_statistics',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field'
            ],
        },
    },
]


WSGI_APPLICATION = 'scroll_manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL)
}



CSRF_TRUSTED_ORIGINS = [
    "https://*.gitpod.io",
    "https://*.herokuapp.com",
    "https://scrollstack-af4b226be9f2.herokuapp.com",
    "http://127.0.0.1:8000"
]

CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Account Setup

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/books/'
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
        ),
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Email backend for development (optional, for testing email features):
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'no-reply@example.com'  # Default fallback email for development
    EMAIL_FAIL_SILENTLY = False
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER', 'no-reply@example.com')
    EMAIL_FAIL_SILENTLY = True
    

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(
    BASE_DIR, 'staticfiles')

# Use Whitenoise for handling static files in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Cloudinary Setup
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    '127.0.0.1',  # or your local IP for other setups
]

# Production logging configuration
import os
import logging
import logging.config

if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'error.log'),
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': True,
            },
        },
    }

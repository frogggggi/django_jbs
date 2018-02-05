#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings for tt1 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys, os.path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4ki$ro=vhvcd7@wnsa^2*f7k+o538a3jv&!lsw8d_n%k$&t4*p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ENABLE_HTTP_REQUEST_LOGGING = False
ENABLE_AUDIT = True

ALLOWED_HOSTS = []


# Application definition

MY_EMAIL='frogggggi@gmail.com'
MY_NAME='Alex'



INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'new_tt1',
    'south',
    'loginsys',
    'myhttprequests',
    'djcelery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'new_tt1.middleware.RequestContentMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'new_tt1.context_processors.tmp_context_processor',
)


ROOT_URLCONF = 'tt1.urls'

WSGI_APPLICATION = 'tt1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'test_pr',
        'PASSWORD': '1111',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/



TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    os.path.join(BASE_DIR,  'loginsys/templates'),
)

#LOGIN_REDIRECT_URL = '/home/'

# work vs files

_PATH = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(_PATH, 'files', 'media')
MEDIA_URL = '/media/'

FIXTURE_DIRS = (
   '/fixtures/',
)

STATIC_ROOT = os.path.join(_PATH, 'files', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(_PATH, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ADMIN_MEDIA_PREFIX = '/static/admin/'

# адрес redis сервера
BROKER_URL = 'redis://localhost:6379/0'
# храним результаты выполнения задач так же в redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# в течение какого срока храним результаты, после чего они удаляются
CELERY_TASK_RESULT_EXPIRES = 7*86400  # 7 days
# это нужно для мониторинга наших воркеров
CELERY_SEND_EVENTS = True
# место хранения периодических задач (данные для планировщика)
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

# в конец settings.py добавляем строчки
import djcelery
djcelery.setup_loader()
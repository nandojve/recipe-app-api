"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from os import environ
from decouple import config
from dj_database_url import parse as dburl

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)
INTERNAL_IPS = ['127.0.0.1']

ALLOWED_HOSTS = ['hero.geo4cities.com', 'peregrine-recipe-app-api.herokuapp.com', 'localhost', '127.0.0.1', '192.168.10.199']

# Application definition
# MANDATORY: debug_toolbar MUST BE last one
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    # Social Auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    # 'allauth.socialaccount.providers.agave',
    # 'allauth.socialaccount.providers.amazon',
    # 'allauth.socialaccount.providers.angellist',
    # 'allauth.socialaccount.providers.asana',
    # 'allauth.socialaccount.providers.auth0',
    # 'allauth.socialaccount.providers.authentiq',
    # 'allauth.socialaccount.providers.baidu',
    # 'allauth.socialaccount.providers.basecamp',
    # 'allauth.socialaccount.providers.bitbucket',
    # 'allauth.socialaccount.providers.bitbucket_oauth2',
    # 'allauth.socialaccount.providers.bitly',
    # 'allauth.socialaccount.providers.cern',
    # 'allauth.socialaccount.providers.coinbase',
    # 'allauth.socialaccount.providers.dataporten',
    # 'allauth.socialaccount.providers.daum',
    # 'allauth.socialaccount.providers.digitalocean',
    # 'allauth.socialaccount.providers.discord',
    # 'allauth.socialaccount.providers.disqus',
    # 'allauth.socialaccount.providers.douban',
    # 'allauth.socialaccount.providers.draugiem',
    # 'allauth.socialaccount.providers.dropbox',
    # 'allauth.socialaccount.providers.dwolla',
    # 'allauth.socialaccount.providers.edmodo',
    # 'allauth.socialaccount.providers.eveonline',
    # 'allauth.socialaccount.providers.evernote',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.feedly',
    # 'allauth.socialaccount.providers.fivehundredpx',
    # 'allauth.socialaccount.providers.flickr',
    # 'allauth.socialaccount.providers.foursquare',
    # 'allauth.socialaccount.providers.fxa',
    # 'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.gitlab',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.hubic',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.jupyterhub',
    # 'allauth.socialaccount.providers.kakao',
    # 'allauth.socialaccount.providers.line',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.linkedin_oauth2',
    # 'allauth.socialaccount.providers.mailru',
    # 'allauth.socialaccount.providers.mailchimp',
    # 'allauth.socialaccount.providers.meetup',
    # 'allauth.socialaccount.providers.microsoft',
    # 'allauth.socialaccount.providers.naver',
    # 'allauth.socialaccount.providers.nextcloud',
    # 'allauth.socialaccount.providers.odnoklassniki',
    # 'allauth.socialaccount.providers.openid',
    # 'allauth.socialaccount.providers.orcid',
    # 'allauth.socialaccount.providers.paypal',
    # 'allauth.socialaccount.providers.patreon',
    # 'allauth.socialaccount.providers.persona',
    # 'allauth.socialaccount.providers.pinterest',
    # 'allauth.socialaccount.providers.reddit',
    # 'allauth.socialaccount.providers.robinhood',
    # 'allauth.socialaccount.providers.sharefile',
    # 'allauth.socialaccount.providers.shopify',
    # 'allauth.socialaccount.providers.slack',
    # 'allauth.socialaccount.providers.soundcloud',
    # 'allauth.socialaccount.providers.spotify',
    # 'allauth.socialaccount.providers.stackexchange',
    # 'allauth.socialaccount.providers.steam',
    # 'allauth.socialaccount.providers.stripe',
    # 'allauth.socialaccount.providers.trello',
    # 'allauth.socialaccount.providers.tumblr',
    # 'allauth.socialaccount.providers.twentythreeandme',
    # 'allauth.socialaccount.providers.twitch',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.untappd',
    # 'allauth.socialaccount.providers.vimeo',
    # 'allauth.socialaccount.providers.vimeo_oauth2',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.weibo',
    # 'allauth.socialaccount.providers.weixin',
    # 'allauth.socialaccount.providers.windowslive',
    # 'allauth.socialaccount.providers.xing',

    # Apps
    'leaflet',
    'bootstrapform',

    #
    'core',

    # Debug
    'debug_toolbar',
]

#                               Site Identification
#                                       \/
# http://localhost:8000/admin/sites/site/1/change/
SITE_ID = 1
# AUTH_USER_MODEL = 'allauthdemo_auth.User'
AUTH_USER_MODEL = 'core.User'
# LOGIN_REDIRECT_URL = '/person/'
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_USERNAME_REQUIRED = True
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_MIN_LENGTH = 3
# ACCOUNT_EMAIL_VERIFICATION = 'none'  # testing...
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# SOCIALACCOUNT_AUTO_SIGNUP = False  # require social accounts to use the signup form ... I think
# For custom sign-up form:
# http://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email'
        ],
        'AUTH_PARAMS': {
            'access_type': 'online'
        }
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# Engine	    Django Backend	                            URL
# PostgreSQL	django.db.backends.postgresql_psycopg2	    postgres://USER:PASSWORD@HOST:PORT/NAME
# PostGIS	    django.contrib.gis.db.backends.postgis	    postgis://USER:PASSWORD@HOST:PORT/NAME
# SQLite	    django.db.backends.sqlite3	                sqlite:///PATH
# SpatiaLite	django.contrib.gis.db.backends.spatialite	spatialite:///PATH

DATABASE_IP = config('DATABASE_IP', default='127.0.0.1')
DATABASE_DEV = 'postgres://' + config('DB_USER') + ':' + config('DB_PASSWORD') + '@' + DATABASE_IP + ':5432/' + config('DB_NAME')
DATABASES = {
    'default': config('DATABASE_URL', default=DATABASE_DEV, cast=dburl),
}

# Force Heroku to connect using postgis backend
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = ['static']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = 'person_list'

GEOS_LIBRARY_PATH = environ.get('GEOS_LIBRARY_PATH')
GDAL_LIBRARY_PATH = environ.get('GDAL_LIBRARY_PATH')

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-27.60780, -48.589997),
    'DEFAULT_ZOOM': 4,
    'MAX_ZOOM': 20,
    'MIN_ZOOM': 3,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': 'Peregrine Consultoria e Serviços',
}

# E-Mail configurations see SendGrid, MailGun, Mandrill
# E-Mail reset works ONLY when suposted user has a valid e-mail filed
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER')
ADMINS = [('Geo4Cities Support Team', 'support@geo4cities.com')]
# EMAIL_SUBJECT_PREFIX = '[Django] '
SERVER_EMAIL = 'postmaster@geo4cities.com'

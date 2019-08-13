#!/usr/bin/env python
import os
from ._custom import *
import django_dev_settings

ALLOWED_HOSTS = ['*']

INSTALLED_APPS+= [
    'corsheaders',                      # pip install django-cors-headers
]

MIDDLEWARE+=[
    'corsheaders.middleware.CorsMiddleware',            # pip install django-cors-headers
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES[0]['OPTIONS']['builtins']=['webpack_loader.templatetags.webpack_loader']

WEBPACK_LOADER = {'DEFAULT':{
    'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.dev.json')
}}
django_dev_settings.load()

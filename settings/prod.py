# DJANGO PRODUCTION SETTINGS
import os
from ._custom import *

ALLOWED_HOSTS = ['*']

GA_ID = os.getenv('GA_ID')

if '1' in str(os.getenv('SECURE_SSL')):
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')




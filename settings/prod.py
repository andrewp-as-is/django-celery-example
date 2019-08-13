# DJANGO PRODUCTION SETTINGS
import os
from ._custom import *

ALLOWED_HOSTS = ['*']

TEMPLATES[0]['OPTIONS']['builtins']=['webpack_loader_db.templatetags.webpack_loader_db']

WEBPACK_LOADER = {'DEFAULT':{
    'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.prod.json')
}}

GA_ID = os.getenv('GA_ID')

if '1' in str(os.getenv('SECURE_SSL')):
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')




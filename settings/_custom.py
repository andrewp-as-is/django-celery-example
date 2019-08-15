#!/usr/bin/env python
import djcelery
import os
from ._base_django import *

djcelery.setup_loader()

# AWS Credentials
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# Celery
BROKER_URL = "sqs://%s:%s@" % (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_DEFAULT_QUEUE = os.getenv('AWS_SQS_QUEUE_NAME')
CELERY_RESULT_BACKEND = None
BROKER_TRANSPORT_OPTIONS = {
    'region': 'us-east-1',
    'polling_interval': 20,
}

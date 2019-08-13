from datetime import datetime
from celery import shared_task

@shared_task
def display_time(x, y):
    print("x = %s" % x)
    print("y = %s" % y)
    print("The time is %s :" % str(datetime.now()))
    return True

"""
celery -A apps.base worker -l info
"""

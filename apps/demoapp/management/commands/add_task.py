from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand
import subprocess
from apps.demoapp.tasks import display_time


class Command(BaseCommand):
    def handle(self, *args, **options):
        display_time.delay(4, 4)

"""
export DJANGO_SETTINGS_MODULE=settings.dev

python manage.py add_task
"""

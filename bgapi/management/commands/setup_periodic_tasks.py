

from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule

class Command(BaseCommand):
    help = 'Sets up periodic tasks for the application'

    def handle(self, *args, **kwargs):
        short_interval, created = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS
        )

        hourly_interval, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.HOURS
        )

        PeriodicTask.objects.update_or_create(
                interval=short_interval,
                name='Fetch users every 10 seconds',
                defaults={'task': 'bgapi.task.fetch_users'},
            )

            # Create or update the hourly interval task
        PeriodicTask.objects.update_or_create(
                interval=hourly_interval,
                name='Import users every hour',
                defaults={'task': 'bgapi.task.fetch_users'},
            )

        self.stdout.write(self.style.SUCCESS('Successfully set up periodic tasks'))

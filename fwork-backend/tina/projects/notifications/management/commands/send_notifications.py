# -*- coding: utf-8 -*-


from django.core.management.base import BaseCommand

from tina.base.utils.iterators import iter_queryset
from tina.projects.notifications.models import HistoryChangeNotification
from tina.projects.notifications.services import send_sync_notifications

from django_pglocks import advisory_lock

class Command(BaseCommand):

    def handle(self, *args, **options):
        with advisory_lock("send-notifications-command", wait=False) as acquired:
            if acquired:
                qs = HistoryChangeNotification.objects.all()
                for change_notification in iter_queryset(qs, itersize=100):
                    try:
                        send_sync_notifications(change_notification.pk)
                    except HistoryChangeNotification.DoesNotExist:
                        pass
            else:
                print("Other process already running")

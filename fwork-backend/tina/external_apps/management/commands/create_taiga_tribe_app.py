
from django.core.management.base import BaseCommand
from tina.external_apps.models import Application


class Command(BaseCommand):
    args = ''
    help = 'Create Tina Tribe external app information'

    def handle(self, *args, **options):
        Application.objects.get_or_create(
            id="8836b290-9f45-11e5-958e-52540016141a",
            name="",
            icon_url="",
            web="",
            description="A task-based employment marketplace for software development.",
            next_url="",
        )

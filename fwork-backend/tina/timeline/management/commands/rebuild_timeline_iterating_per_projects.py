# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.test.utils import override_settings
from django.core.management import call_command

from tina.projects.models import Project


class Command(BaseCommand):
    help = 'Regenerate projects timeline iterating per project'

    @override_settings(DEBUG=False)
    def handle(self, *args, **options):
        total = Project.objects.count()

        for count,project in enumerate(Project.objects.order_by("id")):
            print("***********************************\n",
                  " {}/{} {}\n".format(count+1, total, project.name),
                  "***********************************")
            call_command("rebuild_timeline", project=project.id)

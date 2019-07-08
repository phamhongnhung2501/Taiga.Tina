# -*- coding: utf-8 -*-

import logging
import sys

from django.utils.translation import ugettext as _

from tina.base.mails import mail_builder
from tina.users.models import User
from tina.celery import app
from .importer import PivotalImporter

logger = logging.getLogger('tina.importers.pivotal')


@app.task(bind=True)
def import_project(self, user_id, token, project_id, options):
    user = User.object.get(id=user_id)
    importer = PivotalImporter(user, token)
    try:
        project = importer.import_project(project_id, options)
    except Exception as e:
        # Error
        ctx = {
            "user": user,
            "error_subject": _("Error importing PivotalTracker project"),
            "error_message": _("Error importing PivotalTracker project"),
            "project": project_id,
            "exception": e
        }
        email = mail_builder.importer_import_error(user, ctx)
        email.send()
        logger.error('Error importing PivotalTracker project %s (by %s)', project_id, user, exc_info=sys.exc_info())
    else:
        ctx = {
            "project": project,
            "user": user,
        }
        email = mail_builder.pivotal_import_success(user, ctx)
        email.send()

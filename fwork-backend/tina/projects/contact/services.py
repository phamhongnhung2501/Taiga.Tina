# -*- coding: utf-8 -*-

from tina.base.mails import mail_builder
from tina.celery import app
from tina.front.templatetags.functions import resolve as resolve_front_url
from tina.users.services import get_user_photo_url

from . import models


@app.task
def send_contact_email(contact_entry_id):
    contact_entry = models.ContactEntry.objects.filter(id=contact_entry_id).first()
    if contact_entry is None:
        return

    ctx = {
        "comment": contact_entry.comment,
        "full_name": contact_entry.user.get_full_name(),
        "project_name": contact_entry.project.name,
        "photo_url": get_user_photo_url(contact_entry.user),
        "user_profile_url": resolve_front_url("user", contact_entry.user.username),
        "project_settings_url": resolve_front_url("project-admin", contact_entry.project.slug),
    }
    users = contact_entry.project.get_users(with_admin_privileges=True).exclude(id=contact_entry.user_id)
    addresses = ", ".join([u.email for u in users])
    email = mail_builder.contact_notification(addresses, ctx)
    email.extra_headers["Reply-To"] = ", ".join([contact_entry.user.email])
    email.send()

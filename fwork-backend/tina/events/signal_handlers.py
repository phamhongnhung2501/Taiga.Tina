# -*- coding: utf-8 -*-

from django.db.models import signals

from django.dispatch import receiver

from tina.base.utils.db import get_typename_for_model_instance

from . import middleware as mw
from . import events


def on_save_any_model(sender, instance, created, **kwargs):
    # Ignore any object that can not have project_id
    if not hasattr(instance, "project_id"):
        return
    content_type = get_typename_for_model_instance(instance)

    # Ignore any other events
    if content_type not in events.watched_types:
        return

    sesionid = mw.get_current_session_id()

    type = "change"
    if created:
        type = "create"

    events.emit_event_for_model(instance, sessionid=sesionid, type=type)


def on_delete_any_model(sender, instance, **kwargs):
    # Ignore any object that can not have project_id
    content_type = get_typename_for_model_instance(instance)

    # Ignore any other changes
    if content_type not in events.watched_types:
        return

    sesionid = mw.get_current_session_id()

    events.emit_event_for_model(instance, sessionid=sesionid, type="delete")

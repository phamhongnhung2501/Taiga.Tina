# -*- coding: utf-8 -*-

from django import dispatch
from django.apps import AppConfig

signal_assigned_to = dispatch.Signal(providing_args=["user", "obj"])
signal_assigned_users = dispatch.Signal(providing_args=["user", "obj",
                                                        "new_assigned_users"])
signal_watchers_added = dispatch.Signal(providing_args=["user", "obj",
                                                        "new_watchers"])
signal_members_added = dispatch.Signal(providing_args=["user", "project",
                                                       "new_members"])
signal_mentions = dispatch.Signal(providing_args=["user", "obj",
                                                  "mentions"])
signal_comment = dispatch.Signal(providing_args=["user", "obj",
                                                 "watchers"])
signal_comment_mentions = dispatch.Signal(providing_args=["user", "obj",
                                                          "mentions"])


class NotificationsAppConfig(AppConfig):
    name = "tina.projects.notifications"
    verbose_name = "Notifications"

    def ready(self):
        from . import signals as handlers
        signal_assigned_to.connect(handlers.on_assigned_to)
        signal_assigned_users.connect(handlers.on_assigned_users)
        signal_watchers_added.connect(handlers.on_watchers_added)
        signal_members_added.connect(handlers.on_members_added)
        signal_mentions.connect(handlers.on_mentions)
        signal_comment.connect(handlers.on_comment)
        signal_comment_mentions.connect(handlers.on_comment_mentions)

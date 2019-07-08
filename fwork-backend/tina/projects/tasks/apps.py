# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.apps import apps
from django.db.models import signals


def connect_tasks_signals():
    from tina.projects.tagging import signals as tagging_handlers
    from . import signals as handlers

    # Finished date
    signals.pre_save.connect(handlers.set_finished_date_when_edit_task,
                             sender=apps.get_model("tasks", "Task"),
                             dispatch_uid="set_finished_date_when_edit_task")
    # Tags
    signals.pre_save.connect(tagging_handlers.tags_normalization,
                             sender=apps.get_model("tasks", "Task"),
                             dispatch_uid="tags_normalization_task")


def connect_tasks_close_or_open_us_and_milestone_signals():
    from . import signals as handlers
    # Cached prev object version
    signals.pre_save.connect(handlers.cached_prev_task,
                             sender=apps.get_model("tasks", "Task"),
                             dispatch_uid="cached_prev_task")
    # Open/Close US and Milestone
    signals.post_save.connect(handlers.try_to_close_or_open_us_and_milestone_when_create_or_edit_task,
                              sender=apps.get_model("tasks", "Task"),
                              dispatch_uid="try_to_close_or_open_us_and_milestone_when_create_or_edit_task")
    signals.post_delete.connect(handlers.try_to_close_or_open_us_and_milestone_when_delete_task,
                                sender=apps.get_model("tasks", "Task"),
                                dispatch_uid="try_to_close_or_open_us_and_milestone_when_delete_task")


def connect_tasks_custom_attributes_signals():
    from tina.projects.custom_attributes import signals as custom_attributes_handlers
    signals.post_save.connect(custom_attributes_handlers.create_custom_attribute_value_when_create_task,
                              sender=apps.get_model("tasks", "Task"),
                              dispatch_uid="create_custom_attribute_value_when_create_task")


def connect_all_tasks_signals():
    connect_tasks_signals()
    connect_tasks_close_or_open_us_and_milestone_signals()
    connect_tasks_custom_attributes_signals()


def disconnect_tasks_signals():
    signals.pre_save.disconnect(sender=apps.get_model("tasks", "Task"),
                                dispatch_uid="set_finished_date_when_edit_task")
    signals.pre_save.disconnect(sender=apps.get_model("tasks", "Task"),
                                dispatch_uid="tags_normalization")


def disconnect_tasks_close_or_open_us_and_milestone_signals():
    signals.pre_save.disconnect(sender=apps.get_model("tasks", "Task"),
                                dispatch_uid="cached_prev_task")
    signals.post_save.disconnect(sender=apps.get_model("tasks", "Task"),
                                 dispatch_uid="try_to_close_or_open_us_and_milestone_when_create_or_edit_task")
    signals.post_delete.disconnect(sender=apps.get_model("tasks", "Task"),
                                   dispatch_uid="try_to_close_or_open_us_and_milestone_when_delete_task")


def disconnect_tasks_custom_attributes_signals():
    signals.post_save.disconnect(sender=apps.get_model("tasks", "Task"),
                                 dispatch_uid="create_custom_attribute_value_when_create_task")


def disconnect_all_tasks_signals():
    disconnect_tasks_signals()
    disconnect_tasks_close_or_open_us_and_milestone_signals()
    disconnect_tasks_custom_attributes_signals()


class TasksAppConfig(AppConfig):
    name = "tina.projects.tasks"
    verbose_name = "Tasks"

    def ready(self):
        connect_all_tasks_signals()

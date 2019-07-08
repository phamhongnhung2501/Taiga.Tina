# -*- coding: utf-8 -*-

from django.contrib import admin

from tina.projects.attachments.admin import AttachmentInline
from tina.projects.notifications.admin import WatchedInline
from tina.projects.votes.admin import VoteInline

from . import models


class TaskAdmin(admin.ModelAdmin):
    list_display = ["project", "milestone", "user_story", "ref", "subject",]
    list_display_links = ["ref", "subject",]
    inlines = [WatchedInline, VoteInline]
    raw_id_fields = ["project"]
    search_fields = ["subject", "description", "id", "ref"]

    def get_object(self, *args, **kwargs):
        self.obj = super().get_object(*args, **kwargs)
        return self.obj

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if (db_field.name in ["status", "milestone", "user_story"]
                and getattr(self, 'obj', None)):
            kwargs["queryset"] = db_field.related_model.objects.filter(
                                                      project=self.obj.project)
        elif (db_field.name in ["owner", "assigned_to"]
                and getattr(self, 'obj', None)):
            kwargs["queryset"] = db_field.related_model.objects.filter(
                                         memberships__project=self.obj.project)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if (db_field.name in ["watchers"]
                and getattr(self, 'obj', None)):
            kwargs["queryset"] = db_field.related.parent_model.objects.filter(
                                         memberships__project=self.obj.project)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(models.Task, TaskAdmin)

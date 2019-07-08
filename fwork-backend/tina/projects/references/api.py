# -*- coding: utf-8 -*-

from django.apps import apps

from tina.base import exceptions as exc
from tina.base import response
from tina.base.api import viewsets
from tina.base.api.utils import get_object_or_404
from tina.permissions.services import user_has_perm

from .validators import ResolverValidator
from . import permissions


class ResolverViewSet(viewsets.ViewSet):
    permission_classes = (permissions.ResolverPermission,)

    def list(self, request, **kwargs):
        validator = ResolverValidator(data=request.QUERY_PARAMS)
        if not validator.is_valid():
            raise exc.BadRequest(validator.errors)

        data = validator.data

        project_model = apps.get_model("projects", "Project")
        project = get_object_or_404(project_model, slug=data["project"])

        self.check_permissions(request, "list", project)

        result = {"project": project.pk}

        if data["epic"] and user_has_perm(request.user, "view_epics", project):
            result["epic"] = get_object_or_404(project.epics.all(),
                                               ref=data["epic"]).pk
        if data["us"] and user_has_perm(request.user, "view_us", project):
            result["us"] = get_object_or_404(project.user_stories.all(),
                                             ref=data["us"]).pk
        if data["task"] and user_has_perm(request.user, "view_tasks", project):
            result["task"] = get_object_or_404(project.tasks.all(),
                                               ref=data["task"]).pk
        if data["issue"] and user_has_perm(request.user, "view_issues", project):
            result["issue"] = get_object_or_404(project.issues.all(),
                                                ref=data["issue"]).pk
        if data["milestone"] and user_has_perm(request.user, "view_milestones", project):
            result["milestone"] = get_object_or_404(project.milestones.all(),
                                                    slug=data["milestone"]).pk
        if data["wikipage"] and user_has_perm(request.user, "view_wiki_pages", project):
            result["wikipage"] = get_object_or_404(project.wiki_pages.all(),
                                                   slug=data["wikipage"]).pk

        if data["ref"]:
            ref_found = False  # No need to continue once one ref is found
            try:
                value = int(data["ref"])

                if user_has_perm(request.user, "view_epics", project):
                    epic = project.epics.filter(ref=value).first()
                    if epic:
                        result["epic"] = epic.pk
                        ref_found = True
                if ref_found is False and user_has_perm(request.user, "view_us", project):
                    us = project.user_stories.filter(ref=value).first()
                    if us:
                        result["us"] = us.pk
                        ref_found = True
                if ref_found is False and user_has_perm(request.user, "view_tasks", project):
                    task = project.tasks.filter(ref=value).first()
                    if task:
                        result["task"] = task.pk
                        ref_found = True
                if ref_found is False and user_has_perm(request.user, "view_issues", project):
                    issue = project.issues.filter(ref=value).first()
                    if issue:
                        result["issue"] = issue.pk
            except:
                value = data["ref"]

                if user_has_perm(request.user, "view_wiki_pages", project):
                    wiki_page = project.wiki_pages.filter(slug=value).first()
                    if wiki_page:
                        result["wikipage"] = wiki_page.pk

        return response.Ok(result)

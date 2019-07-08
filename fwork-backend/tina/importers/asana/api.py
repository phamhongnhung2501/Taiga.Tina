# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.conf import settings

from tina.base.api import viewsets
from tina.base import response
from tina.base import exceptions as exc
from tina.base.decorators import list_route
from tina.users.services import get_user_photo_url
from tina.users.gravatar import get_user_gravatar_id

from tina.importers import permissions, exceptions
from tina.importers.services import resolve_users_bindings
from .importer import AsanaImporter
from . import tasks


class AsanaImporterViewSet(viewsets.ViewSet):
    permission_classes = (permissions.ImporterPermission,)

    @list_route(methods=["POST"])
    def list_users(self, request, *args, **kwargs):
        self.check_permissions(request, "list_users", None)

        token = request.DATA.get('token', None)
        project_id = request.DATA.get('project', None)

        if not project_id:
            raise exc.WrongArguments(_("The project param is needed"))

        importer = AsanaImporter(request.user, token)

        try:
            users = importer.list_users(project_id)
        except exceptions.InvalidRequest:
            raise exc.BadRequest(_('Invalid Asana API request'))
        except exceptions.FailedRequest:
            raise exc.BadRequest(_('Failed to make the request to Asana API'))

        for user in users:
            if user['detected_user']:
                user['user'] = {
                    'id': user['detected_user'].id,
                    'full_name': user['detected_user'].get_full_name(),
                    'gravatar_id': get_user_gravatar_id(user['detected_user']),
                    'photo': get_user_photo_url(user['detected_user']),
                }
            del(user['detected_user'])
        return response.Ok(users)

    @list_route(methods=["POST"])
    def list_projects(self, request, *args, **kwargs):
        self.check_permissions(request, "list_projects", None)
        token = request.DATA.get('token', None)
        importer = AsanaImporter(request.user, token)
        try:
            projects = importer.list_projects()
        except exceptions.InvalidRequest:
            raise exc.BadRequest(_('Invalid Asana API request'))
        except exceptions.FailedRequest:
            raise exc.BadRequest(_('Failed to make the request to Asana API'))
        return response.Ok(projects)

    @list_route(methods=["POST"])
    def import_project(self, request, *args, **kwargs):
        self.check_permissions(request, "import_project", None)

        token = request.DATA.get('token', None)
        project_id = request.DATA.get('project', None)
        if not project_id:
            raise exc.WrongArguments(_("The project param is needed"))

        options = {
            "name": request.DATA.get('name', None),
            "description": request.DATA.get('description', None),
            "template": request.DATA.get('template', "scrum"),
            "users_bindings": resolve_users_bindings(request.DATA.get("users_bindings", {})),
            "keep_external_reference": request.DATA.get("keep_external_reference", False),
            "is_private": request.DATA.get("is_private", False),
        }

        if settings.CELERY_ENABLED:
            task = tasks.import_project.delay(request.user.id, token, project_id, options)
            return response.Accepted({"task_id": task.id})

        importer = AsanaImporter(request.user, token)
        project = importer.import_project(project_id, options)
        project_data = {
            "slug": project.slug,
            "my_permissions": ["view_us"],
            "is_backlog_activated": project.is_backlog_activated,
            "is_kanban_activated": project.is_kanban_activated,
        }

        return response.Ok(project_data)

    @list_route(methods=["GET"])
    def auth_url(self, request, *args, **kwargs):
        self.check_permissions(request, "auth_url", None)

        url = AsanaImporter.get_auth_url(
            settings.IMPORTERS.get('asana', {}).get('app_id', None),
            settings.IMPORTERS.get('asana', {}).get('app_secret', None),
            settings.IMPORTERS.get('asana', {}).get('callback_url', None)
        )

        return response.Ok({"url": url})

    @list_route(methods=["POST"])
    def authorize(self, request, *args, **kwargs):
        self.check_permissions(request, "authorize", None)

        code = request.DATA.get('code', None)
        if code is None:
            raise exc.BadRequest(_("Code param needed"))

        try:
            asana_token = AsanaImporter.get_access_token(
                code,
                settings.IMPORTERS.get('asana', {}).get('app_id', None),
                settings.IMPORTERS.get('asana', {}).get('app_secret', None),
                settings.IMPORTERS.get('asana', {}).get('callback_url', None)
            )
        except exceptions.InvalidRequest:
            raise exc.BadRequest(_('Invalid Asana API request'))
        except exceptions.FailedRequest:
            raise exc.BadRequest(_('Failed to make the request to Asana API'))

        return response.Ok({"token": asana_token})

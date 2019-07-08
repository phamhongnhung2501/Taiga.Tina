# -*- coding: utf-8 -*-

import uuid

from django.utils.translation import ugettext as _
from django.conf import settings

from tina.base.api import viewsets
from tina.base import response
from tina.base import exceptions as exc
from tina.base.decorators import list_route
from tina.users.models import AuthData, User
from tina.users.services import get_user_photo_url
from tina.users.gravatar import get_user_gravatar_id

from .importer import TrelloImporter
from tina.importers import permissions
from tina.importers.services import resolve_users_bindings
from . import tasks


class TrelloImporterViewSet(viewsets.ViewSet):
    permission_classes = (permissions.ImporterPermission,)

    @list_route(methods=["POST"])
    def list_users(self, request, *args, **kwargs):
        self.check_permissions(request, "list_users", None)

        token = request.DATA.get('token', None)
        project_id = request.DATA.get('project', None)

        if not project_id:
            raise exc.WrongArguments(_("The project param is needed"))

        importer = TrelloImporter(request.user, token)
        users = importer.list_users(project_id)
        for user in users:
            user['user'] = None
            if not user['email']:
                continue

            try:
                Tina_user = User.objects.get(email=user['email'])
            except User.DoesNotExist:
                continue

            user['user'] = {
                'id': Tina_user.id,
                'full_name': Tina_user.get_full_name(),
                'gravatar_id': get_user_gravatar_id(Tina_user),
                'photo': get_user_photo_url(Tina_user),
            }
        return response.Ok(users)

    @list_route(methods=["POST"])
    def list_projects(self, request, *args, **kwargs):
        self.check_permissions(request, "list_projects", None)
        token = request.DATA.get('token', None)
        importer = TrelloImporter(request.user, token)
        projects = importer.list_projects()
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
            "template": request.DATA.get('template', "kanban"),
            "users_bindings": resolve_users_bindings(request.DATA.get("users_bindings", {})),
            "keep_external_reference": request.DATA.get("keep_external_reference", False),
            "is_private": request.DATA.get("is_private", False),
        }

        if settings.CELERY_ENABLED:
            task = tasks.import_project.delay(request.user.id, token, project_id, options)
            return response.Accepted({"task_id": task.id})

        importer = TrelloImporter(request.user, token)
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

        (oauth_token, oauth_secret, url) = TrelloImporter.get_auth_url()

        (auth_data, created) = AuthData.objects.get_or_create(
            user=request.user,
            key="trello-oauth",
            defaults={
                "value": uuid.uuid4().hex,
                "extra": {},
            }
        )
        auth_data.extra = {
            "oauth_token": oauth_token,
            "oauth_secret": oauth_secret,
        }
        auth_data.save()

        return response.Ok({"url": url})

    @list_route(methods=["POST"])
    def authorize(self, request, *args, **kwargs):
        self.check_permissions(request, "authorize", None)

        try:
            oauth_data = request.user.auth_data.get(key="trello-oauth")
            oauth_token = oauth_data.extra['oauth_token']
            oauth_secret = oauth_data.extra['oauth_secret']
            oauth_verifier = request.DATA.get('code')
            oauth_data.delete()
            trello_token = TrelloImporter.get_access_token(oauth_token, oauth_secret, oauth_verifier)['oauth_token']
        except Exception as e:
            raise exc.WrongArguments(_("Invalid or expired auth token"))

        return response.Ok({
            "token": trello_token
        })

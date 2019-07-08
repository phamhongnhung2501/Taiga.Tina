# -*- coding: utf-8 -*-

from tina.base.api.permissions import (TinaResourcePermission, HasProjectPerm,
                                       IsProjectAdmin, AllowAny,
                                       IsObjectOwner, PermissionComponent)

from tina.permissions.services import is_project_admin
from tina.projects.history.services import get_model_from_key, get_pk_from_key


class IsCommentDeleter(PermissionComponent):
    def check_permissions(self, request, view, obj=None):
        return obj.delete_comment_user and obj.delete_comment_user.get("pk", "not-pk") == request.user.pk


class IsCommentOwner(PermissionComponent):
    def check_permissions(self, request, view, obj=None):
        return obj.user and obj.user.get("pk", "not-pk") == request.user.pk


class IsCommentProjectAdmin(PermissionComponent):
    def check_permissions(self, request, view, obj=None):
        model = get_model_from_key(obj.key)
        pk = get_pk_from_key(obj.key)
        project = model.objects.get(pk=pk)
        return is_project_admin(request.user, project)


class EpicHistoryPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    edit_comment_perms =  IsCommentProjectAdmin() | IsCommentOwner()
    delete_comment_perms = IsCommentProjectAdmin() | IsCommentOwner()
    undelete_comment_perms = IsCommentProjectAdmin() | IsCommentDeleter()
    comment_versions_perms = IsCommentProjectAdmin() | IsCommentOwner()


class UserStoryHistoryPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    edit_comment_perms =  IsCommentProjectAdmin() | IsCommentOwner()
    delete_comment_perms = IsCommentProjectAdmin() | IsCommentOwner()
    undelete_comment_perms = IsCommentProjectAdmin() | IsCommentDeleter()
    comment_versions_perms = IsCommentProjectAdmin() | IsCommentOwner()


class TaskHistoryPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    edit_comment_perms =  IsCommentProjectAdmin() | IsCommentOwner()
    delete_comment_perms = IsCommentProjectAdmin() | IsCommentOwner()
    undelete_comment_perms = IsCommentProjectAdmin() | IsCommentDeleter()
    comment_versions_perms = IsCommentProjectAdmin() | IsCommentOwner()


class IssueHistoryPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    edit_comment_perms =  IsCommentProjectAdmin() | IsCommentOwner()
    delete_comment_perms = IsCommentProjectAdmin() | IsCommentOwner()
    undelete_comment_perms = IsCommentProjectAdmin() | IsCommentDeleter()
    comment_versions_perms = IsCommentProjectAdmin() | IsCommentOwner()


class WikiHistoryPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    edit_comment_perms =  IsCommentProjectAdmin() | IsCommentOwner()
    delete_comment_perms = IsCommentProjectAdmin() | IsCommentOwner()
    undelete_comment_perms = IsCommentProjectAdmin() | IsCommentDeleter()
    comment_versions_perms = IsCommentProjectAdmin() | IsCommentOwner()

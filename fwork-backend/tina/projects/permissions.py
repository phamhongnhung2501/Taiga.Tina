# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

from tina.base.api.permissions import TinaResourcePermission
from tina.base.api.permissions import IsAuthenticated
from tina.base.api.permissions import AllowAny
from tina.base.api.permissions import IsSuperUser
from tina.base.api.permissions import IsObjectOwner
from tina.base.api.permissions import PermissionComponent

from tina.base import exceptions as exc

from tina.permissions.permissions import HasProjectPerm
from tina.permissions.permissions import IsProjectAdmin

from . import models
from . import services


class CanLeaveProject(PermissionComponent):
    def check_permissions(self, request, view, obj=None):
        if not obj or not request.user.is_authenticated():
            return False

        try:
            if not services.can_user_leave_project(request.user, obj):
                raise exc.PermissionDenied(_("You can't leave the project if you are the owner or there are "
                                             "no more admins"))
            return True
        except models.Membership.DoesNotExist:
            return False


class ProjectPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    by_slug_perms = HasProjectPerm('view_project')
    create_perms = IsAuthenticated()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    modules_perms = IsProjectAdmin()
    list_perms = AllowAny()
    change_logo_perms = IsProjectAdmin()
    remove_logo_perms = IsProjectAdmin()
    stats_perms = HasProjectPerm('view_project')
    member_stats_perms = HasProjectPerm('view_project')
    issues_stats_perms = HasProjectPerm('view_project')
    regenerate_epics_csv_uuid_perms = IsProjectAdmin()
    regenerate_userstories_csv_uuid_perms = IsProjectAdmin()
    regenerate_issues_csv_uuid_perms = IsProjectAdmin()
    regenerate_tasks_csv_uuid_perms = IsProjectAdmin()
    delete_epics_csv_uuid_perms = IsProjectAdmin()
    delete_userstories_csv_uuid_perms = IsProjectAdmin()
    delete_issues_csv_uuid_perms = IsProjectAdmin()
    delete_tasks_csv_uuid_perms = IsProjectAdmin()
    tags_perms = HasProjectPerm('view_project')
    tags_colors_perms = HasProjectPerm('view_project')
    like_perms = IsAuthenticated() & HasProjectPerm('view_project')
    unlike_perms = IsAuthenticated() & HasProjectPerm('view_project')
    watch_perms = IsAuthenticated() & HasProjectPerm('view_project')
    unwatch_perms = IsAuthenticated() & HasProjectPerm('view_project')
    create_template_perms = IsSuperUser()
    leave_perms = CanLeaveProject()
    transfer_validate_token_perms = IsAuthenticated() & HasProjectPerm('view_project')
    transfer_request_perms = IsProjectAdmin()
    transfer_start_perms = IsObjectOwner()
    transfer_reject_perms = IsAuthenticated() & HasProjectPerm('view_project')
    transfer_accept_perms = IsAuthenticated() & HasProjectPerm('view_project')
    create_tag_perms = IsProjectAdmin()
    edit_tag_perms = IsProjectAdmin()
    delete_tag_perms = IsProjectAdmin()
    mix_tags_perms = IsProjectAdmin()
    duplicate_perms = IsAuthenticated() & HasProjectPerm('view_project')


class ProjectFansPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_project')
    list_perms = HasProjectPerm('view_project')


class ProjectWatchersPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_project')
    list_perms = HasProjectPerm('view_project')


class MembershipPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_create_perms = IsProjectAdmin()
    resend_invitation_perms = IsProjectAdmin()


# Epics

class EpicStatusPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


# User Stories

class PointsPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


class UserStoryStatusPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


class UserStoryDueDatePermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


# Tasks

class TaskStatusPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


class TaskDueDatePermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()

# Issues

class SeverityPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


class PriorityPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


class IssueStatusPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


class IssueTypePermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


class IssueDueDatePermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


# Project Templates

class ProjectTemplatePermission(TinaResourcePermission):
    retrieve_perms = AllowAny()
    create_perms = IsSuperUser()
    update_perms = IsSuperUser()
    partial_update_perms = IsSuperUser()
    destroy_perms = IsSuperUser()
    list_perms = AllowAny()

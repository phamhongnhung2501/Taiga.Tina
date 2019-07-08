# -*- coding: utf-8 -*-

from tina.base.api.permissions import TinaResourcePermission, AllowAny, IsAuthenticated, IsSuperUser
from tina.permissions.permissions import HasProjectPerm, IsProjectAdmin

from tina.permissions.permissions import CommentAndOrUpdatePerm


class TaskPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_tasks')
    create_perms = HasProjectPerm('add_task')
    update_perms = CommentAndOrUpdatePerm('modify_task', 'comment_task')
    partial_update_perms = CommentAndOrUpdatePerm('modify_task', 'comment_task')
    destroy_perms = HasProjectPerm('delete_task')
    list_perms = AllowAny()
    filters_data_perms = AllowAny()
    csv_perms = AllowAny()
    bulk_create_perms = HasProjectPerm('add_task')
    bulk_update_order_perms = HasProjectPerm('modify_task')
    bulk_update_milestone_perms = HasProjectPerm('modify_task')
    upvote_perms = IsAuthenticated() & HasProjectPerm('view_tasks')
    downvote_perms = IsAuthenticated() & HasProjectPerm('view_tasks')
    watch_perms = IsAuthenticated() & HasProjectPerm('view_tasks')
    unwatch_perms = IsAuthenticated() & HasProjectPerm('view_tasks')


class TaskVotersPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_tasks')
    list_perms = HasProjectPerm('view_tasks')


class TaskWatchersPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_tasks')
    list_perms = HasProjectPerm('view_tasks')

# -*- coding: utf-8 -*-

from tina.base.api.permissions import TinaResourcePermission, AllowAny, IsAuthenticated, IsSuperUser
from tina.permissions.permissions import HasProjectPerm, IsProjectAdmin

from tina.permissions.permissions import CommentAndOrUpdatePerm


class UserStoryPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_us')
    by_ref_perms = HasProjectPerm('view_us')
    create_perms = HasProjectPerm('add_us_to_project') | HasProjectPerm('add_us')
    update_perms = CommentAndOrUpdatePerm('modify_us', 'comment_us')
    partial_update_perms = CommentAndOrUpdatePerm('modify_us', 'comment_us')
    destroy_perms = HasProjectPerm('delete_us')
    list_perms = AllowAny()
    filters_data_perms = AllowAny()
    csv_perms = AllowAny()
    bulk_create_perms = IsAuthenticated() & (HasProjectPerm('add_us_to_project') | HasProjectPerm('add_us'))
    bulk_update_order_perms = HasProjectPerm('modify_us')
    bulk_update_milestone_perms = HasProjectPerm('modify_us')
    upvote_perms = IsAuthenticated() & HasProjectPerm('view_us')
    downvote_perms = IsAuthenticated() & HasProjectPerm('view_us')
    watch_perms = IsAuthenticated() & HasProjectPerm('view_us')
    unwatch_perms = IsAuthenticated() & HasProjectPerm('view_us')


class UserStoryVotersPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_us')
    list_perms = HasProjectPerm('view_us')


class UserStoryWatchersPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_us')
    list_perms = HasProjectPerm('view_us')

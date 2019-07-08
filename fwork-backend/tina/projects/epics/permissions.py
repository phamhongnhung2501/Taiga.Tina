# -*- coding: utf-8 -*-

from tina.base.api.permissions import TinaResourcePermission, AllowAny, IsAuthenticated
from tina.base.api.permissions import IsSuperUser, HasProjectPerm, IsProjectAdmin

from tina.permissions.permissions import CommentAndOrUpdatePerm


class EpicPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_epics')
    create_perms = HasProjectPerm('add_epic')
    update_perms = CommentAndOrUpdatePerm('modify_epic', 'comment_epic')
    partial_update_perms = CommentAndOrUpdatePerm('modify_epic', 'comment_epic')
    destroy_perms = HasProjectPerm('delete_epic')
    list_perms = AllowAny()
    filters_data_perms = AllowAny()
    csv_perms = AllowAny()
    bulk_create_perms = HasProjectPerm('add_epic')
    upvote_perms = IsAuthenticated() & HasProjectPerm('view_epics')
    downvote_perms = IsAuthenticated() & HasProjectPerm('view_epics')
    watch_perms = IsAuthenticated() & HasProjectPerm('view_epics')
    unwatch_perms = IsAuthenticated() & HasProjectPerm('view_epics')


class EpicRelatedUserStoryPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_epics')
    create_perms = HasProjectPerm('modify_epic')
    update_perms = HasProjectPerm('modify_epic')
    partial_update_perms = HasProjectPerm('modify_epic')
    destroy_perms = HasProjectPerm('modify_epic')
    list_perms = AllowAny()
    bulk_create_perms = HasProjectPerm('modify_epic')


class EpicVotersPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_epics')
    list_perms = HasProjectPerm('view_epics')


class EpicWatchersPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_epics')
    list_perms = HasProjectPerm('view_epics')

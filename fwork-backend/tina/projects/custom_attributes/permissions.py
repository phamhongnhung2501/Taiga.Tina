# -*- coding: utf-8 -*-

from tina.base.api.permissions import TinaResourcePermission
from tina.base.api.permissions import HasProjectPerm
from tina.base.api.permissions import IsProjectAdmin
from tina.base.api.permissions import AllowAny
from tina.base.api.permissions import IsSuperUser


######################################################
# Custom Attribute Permissions
#######################################################

class EpicCustomAttributePermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


class UserStoryCustomAttributePermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


class TaskCustomAttributePermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


class IssueCustomAttributePermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
    bulk_update_order_perms = IsProjectAdmin()


######################################################
# Custom Attributes Values Permissions
#######################################################

class EpicCustomAttributesValuesPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_us')
    update_perms = HasProjectPerm('modify_us')
    partial_update_perms = HasProjectPerm('modify_us')


class UserStoryCustomAttributesValuesPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_us')
    update_perms = HasProjectPerm('modify_us')
    partial_update_perms = HasProjectPerm('modify_us')


class TaskCustomAttributesValuesPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_tasks')
    update_perms = HasProjectPerm('modify_task')
    partial_update_perms = HasProjectPerm('modify_task')


class IssueCustomAttributesValuesPermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_issues')
    update_perms = HasProjectPerm('modify_issue')
    partial_update_perms = HasProjectPerm('modify_issue')

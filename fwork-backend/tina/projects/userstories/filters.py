# -*- coding: utf-8 -*-


from tina.base import filters


class EpicFilter(filters.BaseRelatedFieldsFilter):
    filter_name = "epics"
    param_name = "epic"
    exclude_param_name = 'exclude_epic'

# -*- coding: utf-8 -*-


from tina.base.api.permissions import (TinaResourcePermission,
                                       IsProjectAdmin, IsAuthenticated)


class ImportExportPermission(TinaResourcePermission):
    import_project_perms = IsAuthenticated()
    import_item_perms = IsProjectAdmin()
    export_project_perms = IsProjectAdmin()
    load_dump_perms = IsAuthenticated()

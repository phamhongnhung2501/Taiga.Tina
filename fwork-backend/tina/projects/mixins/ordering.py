# -*- coding: utf-8 -*-


from django.utils.translation import ugettext as _

from tina.base import response
from tina.base import exceptions as exc
from tina.base.api.utils import get_object_or_404
from tina.base.decorators import list_route

from tina.projects.models import Project


#############################################
# ViewSets
#############################################

class BulkUpdateOrderMixin:
    """
    This mixin need three fields in the child class:

    - bulk_update_param: that the name of the field of the data received from
      the cliente that contains the pairs (id, order) to sort the objects.
    - bulk_update_perm: that containts the codename of the permission needed to sort.
    - bulk_update_order: method with bulk update order logic
    """

    @list_route(methods=["POST"])
    def bulk_update_order(self, request, **kwargs):
        bulk_data = request.DATA.get(self.bulk_update_param, None)

        if bulk_data is None:
            raise exc.BadRequest(_("'{param}' parameter is mandatory".format(param=self.bulk_update_param)))

        project_id = request.DATA.get('project', None)
        if project_id is None:
            raise exc.BadRequest(_("'project' parameter is mandatory"))

        project = get_object_or_404(Project, id=project_id)

        self.check_permissions(request, 'bulk_update_order', project)
        if project.blocked_code is not None:
            raise exc.Blocked(_("Blocked element"))
            
        self.__class__.bulk_update_order_action(project, request.user, bulk_data)
        return response.NoContent(data=None)

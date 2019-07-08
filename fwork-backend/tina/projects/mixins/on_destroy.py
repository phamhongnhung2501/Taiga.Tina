# -*- coding: utf-8 -*-


from django.db import transaction as tx

from tina.base.api.utils import get_object_or_404


#############################################
# ViewSets
#############################################

class MoveOnDestroyMixin:
    @tx.atomic
    def destroy(self, request, *args, **kwargs):
        move_to = self.request.QUERY_PARAMS.get('moveTo', None)
        if move_to is None:
            return super().destroy(request, *args, **kwargs)

        obj = self.get_object_or_none()
        move_item = get_object_or_404(self.model, id=move_to)

        self.check_permissions(request, 'destroy', obj)

        qs = self.move_on_destroy_related_class.objects.filter(**{self.move_on_destroy_related_field: obj})
        qs.update(**{self.move_on_destroy_related_field: move_item})

        if getattr(obj.project, self.move_on_destroy_project_default_field) == obj:
            setattr(obj.project, self.move_on_destroy_project_default_field, move_item)
            obj.project.save()

        return super().destroy(request, *args, **kwargs)

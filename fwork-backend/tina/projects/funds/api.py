from django.db.models import Q
from django.utils import timezone
# from rest_framework.views import APIView

from tina.base import response
from tina.base.api import ModelCrudViewSet
from tina.base.api import GenericViewSet
from tina.base.api.utils import get_object_or_404


from . import models
# from . import permissions
from . import serializers
# from . import services
# from . import validators
# from . import utils as tasks_utils

class FundTaskViewSet(GenericViewSet):
	serializer_class = serializers.PozitSerializer
	resource_model = models.Fund
	# def check_permissions(self, request, obj=None):
	# 	return obj and request.user.is_authenticated() and \
	# 		   request.user.pk == obj.user_id

	def list(self, request):
		if self.request.user.is_anonymous():
			return response.Ok({})

		queryset = models.Fund.objects \
			.filter(user=self.request.user)

		if request.GET.get("only_unread", False):
			queryset = queryset.filter(read__isnull=True)

		queryset = queryset.order_by('expense','profit')

		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_pagination_serializer(page)
			return response.Ok({
				"objects": serializer.data,
				"total": queryset.count()
			})

		serializer = self.get_serializer(queryset, many=True)
		return response.Ok(serializer.data)

	# def post(self, request):
	# 	# self.check_permissions(request)
	#
	# 	# models.Pozit.objects.filter(user=self.request.user) \
	# 	# 	.update(read=timezone.now())
	# 	models.Pozit.save()
	#
	# 	return response.Ok()

	def post(self, request):
		if self.request.user.is_anonymous():
			return response.Ok({"Wrong!"})

		serializer = self.serializer_class(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
		return response.Ok(serializer.data)
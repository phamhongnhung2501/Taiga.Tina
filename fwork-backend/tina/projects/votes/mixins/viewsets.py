# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist

from tina.base import response
from tina.base.api import viewsets
from tina.base.api.utils import get_object_or_404
from tina.base.decorators import detail_route

from tina.projects.votes import serializers
from tina.projects.votes import services
from tina.projects.votes.utils import attach_total_voters_to_queryset, attach_is_voter_to_queryset


class VotedResourceMixin:
    """
    Note: Update get_queryset method:
           def get_queryset(self):
               qs = super().get_queryset()
               return self.attach_votes_attrs_to_queryset(qs)

    - the classes using this mixing must have a method:
    def pre_conditions_on_save(self, obj)
    """

    @detail_route(methods=["POST"])
    def upvote(self, request, pk=None):
        obj = self.get_object()
        self.check_permissions(request, "upvote", obj)
        self.pre_conditions_on_save(obj)

        services.add_vote(obj, user=request.user)
        return response.Ok()

    @detail_route(methods=["POST"])
    def downvote(self, request, pk=None):
        obj = self.get_object()
        self.check_permissions(request, "downvote", obj)
        self.pre_conditions_on_save(obj)

        services.remove_vote(obj, user=request.user)
        return response.Ok()


class VotersViewSetMixin:
    # Is a ModelListViewSet with two required params: permission_classes and resource_model
    serializer_class = serializers.VoterSerializer
    list_serializer_class = serializers.VoterSerializer
    permission_classes = None
    resource_model = None

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        resource_id = kwargs.get("resource_id", None)
        resource = get_object_or_404(self.resource_model, pk=resource_id)

        self.check_permissions(request, 'retrieve', resource)

        try:
            self.object = services.get_voters(resource).get(pk=pk)
        except ObjectDoesNotExist: # or User.DoesNotExist
            return response.NotFound()

        serializer = self.get_serializer(self.object)
        return response.Ok(serializer.data)

    def list(self, request, *args, **kwargs):
        resource_id = kwargs.get("resource_id", None)
        resource = get_object_or_404(self.resource_model, pk=resource_id)

        self.check_permissions(request, 'list', resource)

        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        resource = self.resource_model.objects.get(pk=self.kwargs.get("resource_id"))
        return services.get_voters(resource)

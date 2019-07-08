from tina.base.api import serializers
from . import models

class PozitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Budget
        fields = ("name","user_story","subject","user","expense", "profit")

# class PozitSerializer():
# # class PozitSerializer(VoteResourceSerializerMixin, WatchedResourceSerializer,OwnerExtraInfoSerializerMixin, AssignedToExtraInfoSerializerMixin,StatusExtraInfoSerializerMixin, ProjectExtraInfoSerializerMixin,BasicAttachmentsInfoSerializerMixin, TaggedInProjectResourceSerializer,TotalCommentsSerializerMixin, DueDateSerializerMixin,serializers.LightSerializer):
# # 	pozit_in = Field()
# # 	pozit_out = Field()
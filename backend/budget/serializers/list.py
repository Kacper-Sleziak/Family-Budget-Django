from rest_framework import serializers

from user.serializers import SimpleUserSerializer
from utils.serializers import QuerySerializerMixin

from ..models.list import List


class ListSerializer(serializers.ModelSerializer):
    users = SimpleUserSerializer(many=True)
    creator = SimpleUserSerializer()

    class Meta:
        model = List
        fields = ["creator", "users"]

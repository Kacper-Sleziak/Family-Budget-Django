from django.db import IntegrityError
from rest_framework import serializers

from user.serializers import SimpleUserSerializer

from ..models.list import List


class ListSerializer(serializers.ModelSerializer):
    users = SimpleUserSerializer(many=True)
    creator = SimpleUserSerializer()

    class Meta:
        model = List
        fields = ["creator", "users"]


class DefaultListSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source="creator__email", read_only=True)

    class Meta:
        model = List
        fields = [
            "creator",
            "users",
        ]

    def save(self):
        user = self.context.get("user")
        try:
            List.objects.create(creator=user)
        except IntegrityError:
            raise serializers.ValidationError("User already has the list!")

from rest_framework import serializers

from utils.serializers import QuerySerializerMixin

from ..models.budget import Budget
from ..serializers.list import ListSerializer


class DefaultBudgetSerializer(serializers.ModelSerializer, QuerySerializerMixin):
    list = ListSerializer()

    RELATED_FIELDS = [
        "list",
    ]

    class Meta:
        model = Budget
        fields = "__all__"

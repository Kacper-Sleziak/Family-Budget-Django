from rest_framework import serializers

from ..models.budget import Budget


class DefaultBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        field = "__all__"

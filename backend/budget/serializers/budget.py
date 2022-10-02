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


class CreateBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ["title", "description", "money", "category"]

    def save(self):
        budget_list = self.context.get("list")
        user = self.context.get("user")
        title = self.validated_data.get("title")
        description = self.validated_data.get("description")
        money = self.validated_data.get("money")
        category = self.validated_data.get("category")

        Budget.objects.create(
            list=budget_list,
            user=user,
            title=title,
            description=description,
            money=money,
            category=category,
        )

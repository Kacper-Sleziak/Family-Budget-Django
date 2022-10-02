from rest_framework import serializers

from ..models.transaction import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    budget = serializers.ReadOnlyField()
    delta_money = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Transaction
        fields = "__all__"

    def save(self):
        budget = self.context.get("budget")
        user = self.context.get("user")
        delta_money = self.validated_data.get("delta_money")

        Transaction.objects.create(budget=budget, delta_money=delta_money, user=user)

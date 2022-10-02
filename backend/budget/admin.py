from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from .models.budget import Budget
from .models.budget_list import BudgetList
from .models.transaction import Transaction

try:

    @admin.register(Budget)
    class BudgetAdmin(admin.ModelAdmin):
        list_display = ("title", "category", "money", "get_creator", "get_transactions")
        list_filter = ("category",)

        @admin.display(description="list creator")
        def get_creator(self, obj):
            return obj.list.creator

        @admin.display(description="transactions")
        def get_transactions(self, obj):
            return format_html_join(
                mark_safe("<br>"),
                "{}",
                (
                    (f"{transaction.delta_money} by {transaction.user.full_name}",)
                    for transaction in Transaction.objects.filter(budget=obj)
                ),
            )

    @admin.register(BudgetList)
    class ListAdmin(admin.ModelAdmin):
        list_display = ("creator", "get_users")

        @admin.display(description="users")
        def get_users(self, obj):
            return format_html_join(
                mark_safe("<br>"),
                "{}",
                ((user.full_name,) for user in obj.users.all()),
            )

    @admin.register(Transaction)
    class TransactionAdmin(admin.ModelAdmin):
        list_display = ("delta_money", "get_budget", "created")

        @admin.display(description="budget")
        def get_budget(self, obj):
            return obj.budget.title

except admin.sites.AlreadyRegistered:
    pass

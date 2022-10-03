import django_filters
from django.db.models import Q

from ..models.budget_list import BudgetList


class BudgetListFilter(django_filters.FilterSet):
    creator = django_filters.CharFilter(method="user_custom_filter", label="Search")

    class Meta:
        model = BudgetList
        fields = [
            "creator",
        ]

    def user_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(creator__first_name__icontains=value)
            | Q(creator__last_name__icontains=value)
            | Q(creator__email__icontains=value)
        )

    ordering = django_filters.OrderingFilter(fields=(("creator", "creator__email"),))

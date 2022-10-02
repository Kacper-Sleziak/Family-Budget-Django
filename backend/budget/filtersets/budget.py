import django_filters

from ..models.budget import Budget


class BudgetFilter(django_filters.FilterSet):
    money = django_filters.RangeFilter()
    title = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    list = django_filters.NumberFilter()

    class Meta:
        model = Budget
        fields = ["list", "title", "description", "money", "category"]

    ordering = django_filters.OrderingFilter(
        fields=(
            ("money", "money"),
            ("title", "title"),
            ("list__creator__email", "creator"),
            ("category", "category"),
        )
    )

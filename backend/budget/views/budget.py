from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..filtersets.budget import BudgetFilter
from ..models.budget import Budget
from ..pagination import StandardPagination
from ..serializers.budget import DefaultBudgetSerializer


class BudgetViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    BudgetViewSet return list of budgets for given params

    Available Params:
    *page
    *money_min
    *money_max
    *list - to get budget for exact list user this param
    """

    queryset = Budget.objects.all()
    serializer_class = DefaultBudgetSerializer
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = BudgetFilter
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        serializer = self.get_serializer()
        return serializer.get_related_queries(queryset)

from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status, views, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.settings import env

from ..filtersets.budget import BudgetFilter
from ..models.budget import Budget
from ..models.budget_list import BudgetList
from ..pagination import StandardPagination
from ..serializers.budget import (CreateBudgetSerializer,
                                  DefaultBudgetSerializer)


class CreateBudget(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, list_pk):
        try:
            budget_list = BudgetList.objects.get(pk=list_pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if not budget_list.has_access(request.user):
            for user in budget_list.users.all():
                return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = CreateBudgetSerializer(
            data=request.data, context={"list": budget_list, "user": request.user}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_201_CREATED,
            )
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class BudgetViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    BudgetViewSet return list of budgets for given params

    Available Params:
    *page
    *money_min
    *money_max
    *category - one of choices from Category model
    *list(id) - to get budget for exact list user this param
    """

    queryset = Budget.objects.all()
    serializer_class = DefaultBudgetSerializer
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = BudgetFilter

    if env("DEBUG"):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        serializer = self.get_serializer()
        return serializer.get_related_queries(queryset)

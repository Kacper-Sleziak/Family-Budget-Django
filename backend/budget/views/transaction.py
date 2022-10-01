from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models.budget import Budget
from ..serializers.transaction import TransactionSerializer


class CreateTransaction(views.APIView):
    """
    View create transaction for given in ulr id and delta_money in body
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, budget_pk):
        try:
            budget = Budget.objects.get(pk=budget_pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        budget_list = budget.list

        if not budget_list.has_access(request.user):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = TransactionSerializer(
            data=request.data, context={"budget": budget}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_201_CREATED,
            )
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

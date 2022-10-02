from django.core.exceptions import ObjectDoesNotExist
from rest_framework import mixins, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.models import User
from utils.permissions import ListCreatorPermission

from ..models.budget_list import BudgetList
from ..serializers.list import DefaultListSerializer


class ListViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = BudgetList.objects.all()
    serializer_class = DefaultListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, ListCreatorPermission]

    def get_serializer_context(self):
        context = super(ListViewSet, self).get_serializer_context()
        context.update({"user": self.request.user})
        return context

    @action(detail=True, methods=["patch"])
    def add_new_user(self, request, pk):
        """
        View add user to List

        Request Body:
        *user - id of user that we want to add to list.users
        """
        user = self.get_object()
        list_of_user = BudgetList.objects.get(pk=user.id)

        try:
            new_user = User.objects.get(pk=int(request.data["user"]))
        except (KeyError, ValueError):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        list_of_user.users.add(new_user)

        return Response(status=status.HTTP_200_OK)

from rest_framework import mixins, views, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


class LoginView(views.APIView):
    pass


class RegisterView(views.APIView):
    pass


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    pass

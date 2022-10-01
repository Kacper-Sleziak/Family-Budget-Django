from rest_framework import mixins, status, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import LoginSerializer, UserSerializer


class LoginView(views.APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(
            data=self.request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        token = Token.objects.get(user=user).key
        feedback_data = UserSerializer(user).data
        feedback_data["token"] = token

        return Response(
            feedback_data,
            status=status.HTTP_200_OK,
        )


class RegisterView(views.APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            account = serializer.save()

            token = Token.objects.get(user=account)
            token_key = token.key
            feedback_data = UserSerializer(account).data
            feedback_data["token"] = token_key
            return Response(feedback_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     pass

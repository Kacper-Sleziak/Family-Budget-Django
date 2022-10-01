from django.contrib.auth import authenticate
from rest_framework import serializers

from utils.serializers import ReadOnlyModelSerializer
from utils.validators import PasswordValidator

from .models import User


class SimpleUserSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
        password = data["password"]
        password2 = data["password2"]

        # Using custom validator
        password_validator = PasswordValidator(password=password)
        password_validator.validate(length=9, password2=password2)
        return data

    def save(self):
        user = User(
            email=self.validated_data["email"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
        )
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """

    email = serializers.CharField(label="email", write_only=True)
    password = serializers.CharField(
        label="Password",
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )

    def validate(self, attrs):
        # Take username and password from request
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(
                request=self.context.get("request"), username=email, password=password
            )
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = "Access denied: wrong username or password."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code="authorization")
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs["user"] = user
        return attrs

from django.contrib import admin
from rest_framework.authtoken.models import Token

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "email",
        "first_name",
        "last_name",
        "get_token",
    )

    @admin.display(description="token")
    def get_token(self, obj):
        return Token.objects.get(user=obj)

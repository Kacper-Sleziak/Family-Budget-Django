from django.db import models

from user.models import User


class BudgetList(models.Model):
    creator = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="creator"
    )
    users = models.ManyToManyField(User, related_name="users", blank=True, default=None)

    class Meta:
        app_label = "budget"

    def is_creator(self, user):
        """
        Check if user have permission to actions like deleting,
        and adding new users to List
        """
        if user == self.creator:
            return True
        return False

    def has_access(self, user):
        """
        Check if user should have access to List
        """
        if user in self.users.all():
            return True
        return False

    def __str__(self):
        return f"List of {self.creator}"

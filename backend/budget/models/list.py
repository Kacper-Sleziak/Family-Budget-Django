from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import User


class List(models.Model):
    creator = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="creator"
    )
    users = models.ManyToManyField(User, related_name="users")

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
        if user in self.users:
            return True
        return False

    def __str__(self):
        return f"List of {self.creator}"


@receiver(post_save, sender=List)
def post_create(sender, instance, created, *args, **kwargs):
    """
    Add Creator of List instance to users
    """
    if not created:
        return

    instance.users.add(instance.creator)
    instance.save()

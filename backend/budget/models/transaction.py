from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import User

from .budget import Budget


class Transaction(models.Model):
    title = models.CharField(max_length=30, default=None, blank=True, null=True)
    delta_money = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, null=False, blank=False
    )
    budget = models.ForeignKey(
        Budget, on_delete=models.CASCADE, null=False, blank=False
    )
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


@receiver(post_save, sender=Transaction)
def create_token_for_user(sender, instance, created=False, *args, **kwargs):
    if created:
        instance.budget.money += instance.delta_money
        instance.budget.save()

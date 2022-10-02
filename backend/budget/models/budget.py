from enum import unique

from django.db import models

from user.models import User

from .budget_list import BudgetList


class Budget(models.Model):
    CATEGORIES_CHOICES = [
        ("Sport", "Sport"),
        ("Health", "Health"),
        ("Insurance", "Insurance"),
        ("Food", "Food"),
        ("Travel", "Travel"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey(BudgetList, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    money = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    category = models.CharField(max_length=15, choices=CATEGORIES_CHOICES)

    class Meta:
        app_label = "budget"

    def __str__(self):
        return f"{self.title}/{self.list.creator}"

from django.db import models

from .list import List


class Budget(models.Model):
    CATEGORIES_CHOICES = [
        ("Sport", "Sport"),
        ("Health", "Health"),
        ("Insurance", "Insurance"),
        ("Food", "Food"),
        ("Travel", "Travel"),
    ]
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    money = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    category = models.CharField(max_length=15, choices=CATEGORIES_CHOICES)

    class Meta:
        app_label = "budget"

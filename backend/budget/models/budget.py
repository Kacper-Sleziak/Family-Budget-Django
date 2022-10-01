from django.db import models

from .category import Category
from .list import List


class Budget(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    money = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        app_label = "budget"

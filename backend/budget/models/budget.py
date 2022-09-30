from django.db import models

from .list import List


class Budget(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    class Meta:
        app_label = "budget"

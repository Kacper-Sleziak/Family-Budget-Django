from django.db import models

from .list import List


class Category(models.Model):
    header = models.CharField(max_length=30)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    class Meta:
        app_label = "budget"

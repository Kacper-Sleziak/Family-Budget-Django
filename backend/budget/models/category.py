from django.db import models


class Category(models.Model):
    CATEGORIES_CHOICES = [
        ("Sport", "Sport"),
        ("Health", "Health"),
        ("Insurance", "Insurance"),
        ("Food", "Food"),
        ("Travel", "Travel"),
    ]
    header = models.CharField(max_length=15, choices=CATEGORIES_CHOICES)

    class Meta:
        app_label = "budget"

    def __str__(self):
        return self.header

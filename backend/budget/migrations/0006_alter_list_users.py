# Generated by Django 4.1.1 on 2022-10-01 12:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("budget", "0005_alter_category_header"),
    ]

    operations = [
        migrations.AlterField(
            model_name="list",
            name="users",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                related_name="users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

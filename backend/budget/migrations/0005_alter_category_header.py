# Generated by Django 4.1.1 on 2022-10-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("budget", "0004_remove_category_list_budget_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="header",
            field=models.CharField(
                choices=[
                    ("Sport", "Sport"),
                    ("Health", "Health"),
                    ("Insurance", "Insurance"),
                    ("Food", "Food"),
                    ("Travel", "Travel"),
                ],
                max_length=15,
            ),
        ),
    ]
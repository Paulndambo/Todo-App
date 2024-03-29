# Generated by Django 4.1.6 on 2023-03-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="status",
            field=models.CharField(
                choices=[
                    ("todo", "Todo"),
                    ("progress", "Progress"),
                    ("blocked", "Blocked"),
                    ("done", "Done"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="todo",
            name="title",
            field=models.CharField(max_length=255, null=True),
        ),
    ]

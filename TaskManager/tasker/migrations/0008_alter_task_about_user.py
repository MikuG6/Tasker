# Generated by Django 4.1.5 on 2023-01-13 03:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tasker", "0007_task_about_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task_about",
            name="user",
            field=models.ManyToManyField(
                related_name="entries", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]

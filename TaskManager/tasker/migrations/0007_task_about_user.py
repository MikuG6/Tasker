# Generated by Django 4.1.5 on 2023-01-12 10:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tasker", "0006_remove_task_about_title21"),
    ]

    operations = [
        migrations.AddField(
            model_name="task_about",
            name="user",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

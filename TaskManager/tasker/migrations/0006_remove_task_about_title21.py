# Generated by Django 4.1.5 on 2023-01-09 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasker", "0005_task_about_title21"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task_about",
            name="title21",
        ),
    ]

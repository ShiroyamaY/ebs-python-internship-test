# Generated by Django 4.2.18 on 2025-07-30 11:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="enabled",
            field=models.BooleanField(default=True),
        ),
    ]

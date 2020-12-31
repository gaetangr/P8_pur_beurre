# Generated by Django 3.0.11 on 2020-12-31 11:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_favorite"),
    ]

    operations = [
        migrations.AddField(
            model_name="favorite",
            name="user",
            field=models.ForeignKey(
                default="no user",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

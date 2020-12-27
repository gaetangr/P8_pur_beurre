# Generated by Django 3.0.11 on 2020-12-26 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="This is shown on the navbar",
                max_length=255,
                verbose_name="Name of User",
            ),
        ),
    ]
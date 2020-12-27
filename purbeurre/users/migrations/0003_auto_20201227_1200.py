# Generated by Django 3.0.11 on 2020-12-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20201226_2023"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="name",
        ),
        migrations.AlterField(
            model_name="user",
            name="bio",
            field=models.TextField(
                blank=True,
                help_text="Tell the world about yourself, what products do you like etc.",
                verbose_name="Bio",
            ),
        ),
    ]
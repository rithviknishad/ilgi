# Generated by Django 5.1.2 on 2024-11-25 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ilgi", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="energylog",
            old_name="energy_gained",
            new_name="energy_delta",
        ),
    ]

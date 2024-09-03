# Generated by Django 4.2.15 on 2024-09-03 13:50

from django.db import migrations, models

import auto_validator.core.models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_alter_hotkey_hotkey_alter_subnetslot_subnet"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="operator",
            name="email",
        ),
        migrations.RemoveField(
            model_name="subnet",
            name="running_mainnet",
        ),
        migrations.RemoveField(
            model_name="subnet",
            name="running_testnet",
        ),
        migrations.AlterField(
            model_name="hotkey",
            name="hotkey",
            field=models.CharField(
                max_length=48, unique=True, validators=[auto_validator.core.models.validate_hotkey_length]
            ),
        ),
        migrations.AlterField(
            model_name="server",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="server",
            name="ssh_private_key",
            field=models.CharField(blank=True, help_text="Path to the SSH private key file", max_length=255, null=True),
        ),
    ]

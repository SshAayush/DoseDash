# Generated by Django 5.0.1 on 2024-02-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dosedashapp", "0002_transaction"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="Transaction_Status",
            field=models.BooleanField(default=False),
        ),
    ]
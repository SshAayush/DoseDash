# Generated by Django 5.0.1 on 2024-02-10 06:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dosedashapp", "0003_transaction_transaction_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="Transaction_Status",
            field=models.CharField(max_length=300),
        ),
    ]

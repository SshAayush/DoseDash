# Generated by Django 5.0.1 on 2024-02-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dosedashapp", "0005_reminder"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reminder",
            name="Reminder_Date",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="Transaction_Date",
            field=models.DateTimeField(),
        ),
    ]

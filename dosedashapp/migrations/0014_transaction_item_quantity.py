# Generated by Django 5.0.1 on 2024-03-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "dosedashapp",
            "0013_rename_address_userprofile_country_userprofile_area_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="Item_Quantity",
            field=models.ManyToManyField(blank=True, to="dosedashapp.cart"),
        ),
    ]

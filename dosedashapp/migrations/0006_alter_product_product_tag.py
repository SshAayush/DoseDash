# Generated by Django 5.0.1 on 2024-02-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dosedashapp", "0005_alter_product_product_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="Product_Tag",
            field=models.CharField(max_length=100),
        ),
    ]

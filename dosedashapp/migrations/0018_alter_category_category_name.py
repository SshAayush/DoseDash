# Generated by Django 5.0.1 on 2024-03-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosedashapp', '0017_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.DateTimeField(),
        ),
    ]
# Generated by Django 4.2.7 on 2025-01-25 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_remove_products_quantity_products_porcia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='porcia',
            field=models.CharField(default=0, max_length=150, verbose_name='Порция'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_total_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_paid',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

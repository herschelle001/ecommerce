# Generated by Django 3.2.8 on 2021-10-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20211011_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_paid',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-23 08:00

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/', validators=[]),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_alternate',
            field=models.ImageField(default='images/img2_SUlRxwK.png', upload_to='images/', validators=[]),
        ),
    ]
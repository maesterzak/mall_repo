# Generated by Django 3.0.8 on 2020-11-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0043_auto_20201125_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='shipping_method',
            field=models.ManyToManyField(default='Unknown', to='store.ShipMethod'),
        ),
    ]
# Generated by Django 3.0.8 on 2020-11-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_auto_20201103_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_method',
            field=models.CharField(default='Unkown', max_length=30),
        ),
    ]
# Generated by Django 3.0.8 on 2020-09-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20200906_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='complete_customer',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='complete_seller',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
# Generated by Django 3.0.8 on 2020-11-17 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0033_alert_system_money_withdrawal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='store_name',
            field=models.CharField(max_length=17, null=True),
        ),
    ]

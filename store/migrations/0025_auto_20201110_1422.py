# Generated by Django 3.0.8 on 2020-11-10 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_order_order_method'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_method',
            new_name='method',
        ),
    ]

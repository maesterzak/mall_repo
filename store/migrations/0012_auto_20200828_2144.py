# Generated by Django 3.0.8 on 2020-08-28 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20200828_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='about_owner',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='description_store',
            field=models.TextField(max_length=300, null=True),
        ),
    ]

# Generated by Django 3.0.8 on 2020-11-25 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0044_auto_20201125_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmethod',
            name='description',
            field=models.CharField(default='Unknown', max_length=300),
        ),
    ]
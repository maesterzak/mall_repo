# Generated by Django 3.0.8 on 2020-08-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20200827_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='about_owner',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='description_store',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
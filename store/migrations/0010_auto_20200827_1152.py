# Generated by Django 3.0.8 on 2020-08-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20200825_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default store.png', null=True, upload_to=''),
        ),
    ]

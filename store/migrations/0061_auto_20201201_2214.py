# Generated by Django 3.0.8 on 2020-12-01 21:14

from django.db import migrations
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0060_workerdetails_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admindetails',
            name='image',
        ),
        migrations.AlterField(
            model_name='workerdetails',
            name='image',
            field=smartfields.fields.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
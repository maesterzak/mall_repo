# Generated by Django 3.0.8 on 2020-12-01 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0059_workerdetails_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerdetails',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]

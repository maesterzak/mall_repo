# Generated by Django 3.0.8 on 2020-11-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_alert_system_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert_system',
            old_name='status',
            new_name='receiver_status',
        ),
        migrations.AddField(
            model_name='alert_system',
            name='sender_status',
            field=models.CharField(default='Unread', max_length=40),
        ),
    ]

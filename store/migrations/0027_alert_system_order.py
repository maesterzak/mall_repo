# Generated by Django 3.0.8 on 2020-11-13 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_alert_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert_system',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Order'),
        ),
    ]

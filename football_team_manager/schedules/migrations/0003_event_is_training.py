# Generated by Django 5.1.3 on 2024-12-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_training',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

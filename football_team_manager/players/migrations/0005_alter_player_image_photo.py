# Generated by Django 5.1.3 on 2024-11-19 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_remove_player_image_url_player_image_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image_photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]

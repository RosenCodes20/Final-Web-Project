# Generated by Django 5.1.3 on 2024-12-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_alter_player_image_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image_photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
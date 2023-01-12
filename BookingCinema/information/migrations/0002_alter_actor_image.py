# Generated by Django 4.1.5 on 2023-01-12 03:45

from django.db import migrations, models
import information.models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='image',
            field=models.ImageField(default='media/default/user.png', max_length=255, upload_to=information.models.Actor.image_upload_to),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-12 03:39

from django.db import migrations, models
import information.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=255)),
                ('date', models.DateTimeField(null=True)),
                ('image', models.ImageField(default='default/user.png', max_length=255, upload_to=information.models.Actor.image_upload_to)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directors_name', models.CharField(max_length=255)),
                ('year_of_birth', models.DateTimeField(null=True)),
                ('image', models.ImageField(default='default/user.png', max_length=500, upload_to=information.models.Directors.image_upload_to)),
                ('descripton', models.TextField(null=True)),
            ],
        ),
    ]

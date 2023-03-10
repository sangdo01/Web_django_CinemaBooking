# Generated by Django 4.1.5 on 2023-01-12 03:39

from django.db import migrations, models
import django.db.models.deletion
import movie.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('trailer', models.CharField(max_length=500, null=True)),
                ('movie_pic', models.ImageField(default='default/no_image.png', max_length=500, upload_to=movie.models.Movie.image_movie_upload_to)),
                ('banner', models.ImageField(default='default/no_image.png', max_length=500, upload_to=movie.models.Movie.image_banner_upload_to)),
                ('time_of_movie', models.IntegerField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('release_date', models.DateTimeField(null=True)),
                ('is_showing', models.IntegerField(default=2)),
                ('status', models.IntegerField(default=2)),
                ('directors_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.directors')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_genre_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Phim_TheLoaiPhim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie_genre')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dien_vien_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.actor')),
                ('phim_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-11 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('cover_image', models.URLField(blank=True, null=True, verbose_name='Imagen de portada')),
                ('label', models.CharField(blank=True, max_length=150, null=True, verbose_name='Etiqueta de album')),
                ('nb_tracks', models.IntegerField(blank=True, default=0, null=True, verbose_name='Número de Pistas')),
                ('duration', models.IntegerField(default=0)),
                ('fans', models.IntegerField(blank=True, default=0, null=True, verbose_name='Número de Fans')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Fecha de lanzamiento')),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('nb_album', models.IntegerField(blank=True, default=0, null=True)),
                ('tracklist', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'artists',
            },
        ),
        migrations.CreateModel(
            name='TypeOfFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'type_of_file',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('readable', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('title_short', models.CharField(max_length=100)),
                ('title_version', models.CharField(max_length=50)),
                ('isrc', models.CharField(blank=True, max_length=50, null=True)),
                ('duration', models.IntegerField(default=0)),
                ('track_position', models.IntegerField(default=0)),
                ('disk_number', models.IntegerField(default=1)),
                ('rank', models.IntegerField(default=0)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('explicit_lyrics', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_list', to='songs.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='songs.artist')),
                ('contributors', models.ManyToManyField(related_name='collaborated_tracks', to='songs.artist')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='songs.typeoffile')),
            ],
            options={
                'db_table': 'Tracks',
            },
        ),
        migrations.AddField(
            model_name='artist',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artists', to='songs.typeoffile'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='songs.artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='songs.typeoffile'),
        ),
    ]
# Generated by Django 4.1.5 on 2023-01-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_alter_artist_image_alter_artist_nb_album_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='nb_fan',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Número de fans'),
        ),
    ]

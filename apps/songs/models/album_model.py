from django.db import models

from apps.songs.models.type_of_file_model import TypeOfFile
from apps.songs.models.artist_model import Artist

class Album(models.Model):
  title = models.CharField(verbose_name='Título', max_length=100)
  cover_image = models.URLField(verbose_name='Imagen de portada', null=True, blank=True)
  label = models.CharField(verbose_name='Etiqueta de album', max_length=150, null=True, blank=True)
  nb_tracks = models.IntegerField(verbose_name='Número de Pistas', default=0, null=True, blank=True)
  duration = models.IntegerField(default=0)
  fans = models.IntegerField(verbose_name='Número de Fans',default=0, null=True, blank=True)
  release_date = models.DateField(verbose_name='Fecha de lanzamiento', null=True, blank=True)
  available = models.BooleanField(default=True)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
  type = models.ForeignKey(TypeOfFile, on_delete=models.CASCADE, related_name='albums')

  class Meta:
    db_table = 'albums'

  def __str__(self):
    return self.title
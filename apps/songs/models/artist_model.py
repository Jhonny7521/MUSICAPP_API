from django.db import models

from apps.songs.models.type_of_file_model import TypeOfFile 

class Artist(models.Model):
  name = models.CharField(verbose_name='Nombre', max_length=100, unique=True)
  image = models.URLField(verbose_name='Url de imagen',null=True, blank = True)
  nb_album = models.IntegerField(verbose_name='Número de albumes',default=0, null=True, blank = True)
  nb_fan = models.IntegerField(verbose_name='Número de fans',default=0, null=True, blank = True)
  tracklist = models.URLField(verbose_name='Url Lista de reproduccion',max_length=200, null=True, blank = True)
  type = models.ForeignKey(TypeOfFile, on_delete=models.CASCADE, related_name='artists', null=True, blank = True)
  created_at = models.DateField(auto_now_add=True)

  class Meta:
    db_table = "artists"

  def __str__(self) -> str:
    return self.name
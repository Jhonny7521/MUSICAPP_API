from django.db import models

from apps.songs.models.type_of_file_model import TypeOfFile
from apps.songs.models.artist_model import Artist
from apps.songs.models.album_model import Album


class Track(models.Model):
  readable = models.BooleanField(default=True)
  title = models.CharField(max_length=200)
  title_short = models.CharField(max_length=100, null=True, blank=True)
  title_version = models.CharField(max_length=50, null=True, blank=True)
  isrc = models.CharField(max_length=50, null=True, blank=True)
  duration = models.IntegerField(default=0, null=True, blank=True)
  track_position = models.IntegerField(default=0, null=True, blank=True)
  disk_number = models.IntegerField(default=1, null=True, blank=True)
  rank = models.IntegerField(default=0, null=True, blank=True)
  release_date = models.DateField(null=True, blank=True)
  explicit_lyrics = models.BooleanField(default=False, null=True, blank=True)
  contributors = models.ManyToManyField(Artist, related_name='collaborated_tracks', blank=True)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='tracks')
  album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='track_list', null=True, blank=True)
  type = models.ForeignKey(TypeOfFile, on_delete=models.CASCADE, related_name='tracks')
  created_at = models.DateField(auto_now_add=True)

  class Meta:
    db_table = 'tracks'
  
  def __str__(self) -> str:
    return self.title
from rest_framework import serializers

from apps.songs.models.album_model import Album
from apps.songs.api.serializers.validators import is_valid_url

class AlbumSerializer(serializers.ModelSerializer):

  class Meta:
    model = Album
    fields = '__all__'

  def validate_url(self, value:str)->str:
    if not is_valid_url(value):
      raise serializers.ValidationError("Invalid URL or inaccessible URL")

    return value


  def to_representation(self, instance):
    return {
      'id': instance.id,
      'title': instance.title,
      'cover_image': instance.cover_image,
      'label': instance.label,
      'nb_tracks': instance.nb_tracks,
      'duration': instance.duration,
      'fans': instance.fans,
      'release_date': instance.release_date,
      'available': instance.available,
      'artist': {
        'id': instance.artist.id,
        'name': instance.artist.name,
        'image': instance.artist.image,
        'nb_album': instance.artist.nb_album,
        'nb_fan': instance.artist.nb_fan,
        'tracklist': instance.artist.tracklist,
        'type': instance.artist.type.name
        },
      'type': instance.type.name,

    }

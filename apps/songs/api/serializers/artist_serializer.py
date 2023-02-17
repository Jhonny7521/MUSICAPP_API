import requests

from rest_framework import serializers

from apps.songs.models.artist_model import Artist
from apps.songs.api.serializers.validators import is_valid_url

class ArtistSerializer(serializers.ModelSerializer):

  class Meta:
    model = Artist
    fields = '__all__'

  def validate_url(self, value:str)->str:
    if not is_valid_url(value):
      raise serializers.ValidationError("Invalid URL or inaccessible URL")

    return value

  def to_representation(self, instance):
    return {
      'id': instance.id,
      'name': instance.name,
      'image': instance.image,
      'nb_album': instance.nb_album,
      'nb_fan': instance.nb_fan,
      'tracklist': instance.tracklist,
      'type': instance.type.name
    }

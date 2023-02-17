from rest_framework import serializers

from apps.songs.models.tracks_model import Track
from apps.songs.models.album_model import Album
from apps.songs.models.artist_model import Artist

class TrackSerializer(serializers.ModelSerializer):

  class Meta:
    model = Track
    fields = '__all__'

  def validate_album(self, value):
    album_exist = Track.objects.filter(pk=value.id).first()
    if album_exist is None:
      print("El album no existe")
      raise serializers.ValidationError("El album no existe")
    
    return value
  
  def validate_artist(self, value):
    artist_exist = Artist.objects.filter(pk=value.id).first()
    if artist_exist is None:
      print("El artista no existe")
      raise serializers.ValidationError("El artista no existe")
    
    return value

  def create(self, validated_data):
    album = validated_data.get('album')
    album_exists = Album.objects.filter(title=album.title).first()

    if album_exists != None :
      album.nb_tracks += 1
      album.duration += validated_data.get('duration')
      album.save()

    track = super().create(validated_data)

    return track


  def to_representation(self, instance):
    contributors_list = [{
      'id': artist.id,
      'name': artist.name,
      'image': artist.image,
      'nb_album': artist.nb_album,
      'nb_fan': artist.nb_fan,
      'tracklist': artist.tracklist,
      'type': artist.type.name
      } 
      for artist in instance.contributors.all()]

    return {
      'id': instance.id,
      'readable': instance.readable,
      'title': instance.title,
      'title_short': instance.title_short,
      'title_version': instance.title_version,
      'isrc': instance.isrc,
      'duration': instance.duration,
      'track_position': instance.track_position,
      'rank': instance.rank,
      'release_date': instance.release_date,
      'explicit_lyrics': instance.explicit_lyrics,
      'contributors': contributors_list,
      'artist': {
        'id': instance.artist.id,
        'name': instance.artist.name,
        'image': instance.artist.image,
        'nb_album': instance.artist.nb_album,
        'nb_fan': instance.artist.nb_fan,
        'tracklist': instance.artist.tracklist,
        'type': instance.artist.type.name
        },
      'album': {
        'id': instance.album.id,
        'title': instance.album.title,
        'cover_image': instance.album.cover_image,
        'label': instance.album.label,
        'nb_tracks': instance.album.nb_tracks,
        'duration': instance.album.duration,
        'fans': instance.album.fans,
        'release_date': instance.album.release_date,
        'available': instance.album.available,
        'artist': {
          'id': instance.album.artist.id,
          'name': instance.album.artist.name,
          'image': instance.album.artist.image,
          'nb_album': instance.album.artist.nb_album,
          'nb_fan': instance.album.artist.nb_fan,
          'tracklist': instance.album.artist.tracklist,
          'type': instance.album.artist.type.name
          },
        'type': instance.album.type.name,
      },
      'type': instance.type.name,
    }


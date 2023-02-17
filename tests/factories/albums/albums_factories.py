from faker import Faker

from apps.songs.models.album_model import Album

from tests.factories.typeOfFile.type_of_file_factories import TypeOfFileFactory
from tests.factories.artists.artist_factories import ArtistFactory

faker = Faker()

class AlbumsFactory:

  def build_album_JSON(self, type, artist):
    return {
      "title": faker.name(),
      "nb_tracks": 0,
      "duration": 0,
      "fans": 0,
      "release_date": "2021-03-25",
      "available": True,
      "artist": artist,
      "type": type
    }


  def create_album(self, type, artist):
    album, _ = Album.objects.get_or_create(**self.build_album_JSON(type, artist))
    return album
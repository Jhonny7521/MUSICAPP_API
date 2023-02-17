from faker import Faker

from apps.songs.models.artist_model import Artist

faker = Faker()

class ArtistFactory:

  def build_artist_JSON(self, type):
    return {
      "name": faker.name(),
      "image": "",
      "nb_album": 0,
      "nb_fan": 0,
      "type": type
    }

  def create_artist(self, type):
    artist, _ = Artist.objects.get_or_create(**self.build_artist_JSON(type))
    return artist
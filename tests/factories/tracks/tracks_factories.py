from faker import Faker

from apps.songs.models.tracks_model import Track

faker = Faker()

class TracksFactory:

  def build_track_JSON(self, type, artist, album):
    return {
      "readable": True,
      "title": faker.name(),
      "title_short": faker.name(),
      "title_version": "",
      "isrc": "",
      "duration": 107,
      "track_position": 0,
      "rank": 0,
      "release_date": "2022-03-25",
      "explicit_lyrics": False,
      "artist": artist,
      "album": album,
      "type": type
    }


  def create_track(self, type, artist, album):
    track, _ = Track.objects.get_or_create(**self.build_track_JSON(type, artist, album))
    return track
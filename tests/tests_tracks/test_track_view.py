from faker import Faker

from rest_framework import status

from tests.test_config import TestSetUp
from tests.factories.tracks.tracks_factories import TracksFactory
from tests.factories.albums.albums_factories import AlbumsFactory
from tests.factories.artists.artist_factories import ArtistFactory
from tests.factories.typeOfFile.type_of_file_factories import TypeOfFileFactory

faker = Faker()

class TrackTestCase(TestSetUp):
  url = '/tracks/'

  def test_search_all_Tracks(self):
    
    response = self.client.get(self.url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_search_one_track(self):

    type_artist = TypeOfFileFactory().create_type_of_file('artist')
    type_album = TypeOfFileFactory().create_type_of_file('album')
    type_track = TypeOfFileFactory().create_type_of_file('track')
    artist = ArtistFactory().create_artist(type_artist)
    album = AlbumsFactory().create_album(type_album, artist)
    track = TracksFactory().create_track(type_track, artist, album)
    
    response = self.client.get(self.url + str(track.id) + '/')

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_search_track_error(self):
    response = self.client.get(
      self.url + '/5324/',
      format='json'
    )

    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_update_album(self):

    type_artist = TypeOfFileFactory().create_type_of_file('artist')
    type_album = TypeOfFileFactory().create_type_of_file('album')
    type_track = TypeOfFileFactory().create_type_of_file('track')
    artist = ArtistFactory().create_artist(type_artist)
    album = AlbumsFactory().create_album(type_album, artist)
    track = TracksFactory().create_track(type_track, artist, album)

    new_data ={
      "readable": True,
      "title": track.title,
      "title_short": track.title_short,
      "title_version": "",
      "isrc": "",
      "duration": 60,
      "track_position": 1,
      "rank": 1,
      "release_date": "2022-03-25",
      "explicit_lyrics": False,
      "artist": artist.id,
      "album": album.id,
      "type": type_track.id
    }

    response = self.client.put(
      self.url + str(album.id) + '/',
      new_data,
      format='json'
    )

    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  def test_delete_album(self):

    type_artist = TypeOfFileFactory().create_type_of_file('artist')
    type_album = TypeOfFileFactory().create_type_of_file('album')
    type_track = TypeOfFileFactory().create_type_of_file('track')
    artist = ArtistFactory().create_artist(type_artist)
    album = AlbumsFactory().create_album(type_album, artist)
    track = TracksFactory().create_track(type_track, artist, album)

    response = self.client.delete(
      self.url + str(track.id) + '/',
      format='json'
    )

    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
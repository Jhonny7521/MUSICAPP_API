from faker import Faker

from rest_framework import status

from apps.songs.models.album_model import Album

from tests.test_config import TestSetUp
from tests.factories.albums.albums_factories import AlbumsFactory
from tests.factories.artists.artist_factories import ArtistFactory
from tests.factories.typeOfFile.type_of_file_factories import TypeOfFileFactory

faker = Faker()

class AlbumTestCase(TestSetUp):
  url = '/album/'

  def test_search_all_albums(self):
    
    response = self.client.get(self.url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_search_one_album(self):
    type_artist = TypeOfFileFactory().create_type_of_file('artist')
    type_album = TypeOfFileFactory().create_type_of_file('album')
    artist = ArtistFactory().create_artist(type_artist)
    album = AlbumsFactory().create_album(type_album, artist)
    
    response = self.client.get(self.url + str(album.id) + '/')

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_search_album_error(self):
    response = self.client.get(
      self.url + '/5324/',
      format='json'
    )

    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_new_album(self):
    
    type_artist = TypeOfFileFactory().create_type_of_file('artist')
    type_album = TypeOfFileFactory().create_type_of_file('album')
    artist = ArtistFactory().create_artist(type_artist)

    album ={
      "title": faker.name(),
      "nb_tracks": 0,
      "duration": 0,
      "fans": 0,
      "release_date": "2021-03-25",
      "available": True,
      "artist": artist.id,
      "type": type_album.id
    }
    response = self.client.post(
      self.url,
      album,
      format='json'
    )

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Album.objects.all().count(), 1)
    self.assertEqual(response.data['message'], 'Álbum creado correctamente')

  def test_update_album(self):

    type_artist = TypeOfFileFactory().create_type_of_file('artist')
    type_album = TypeOfFileFactory().create_type_of_file('album')
    artist = ArtistFactory().create_artist(type_artist)
    album = AlbumsFactory().create_album(type_album, artist)

    new_data ={
      "title": album.title,
      "nb_tracks": 0,
      "duration": 0,
      "fans": 1,
      "release_date": album.release_date,
      "available": False,
      "artist": artist.id,
      "type": type_album.id
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
    artist = ArtistFactory().create_artist(type_artist)
    album = AlbumsFactory().create_album(type_album, artist)

    response = self.client.delete(
      self.url + str(album.id) + '/',
      format='json'
    )

    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




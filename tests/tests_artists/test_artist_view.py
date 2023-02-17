from faker import Faker

from rest_framework import status

from apps.songs.models.artist_model import Artist
from apps.songs.models.type_of_file_model import TypeOfFile

from tests.test_config import TestSetUp
from tests.factories.artists.artist_factories import ArtistFactory
from tests.factories.typeOfFile.type_of_file_factories import TypeOfFileFactory

faker = Faker()

class ArtistTestCase(TestSetUp):
  url = '/artist/'

  def test_search_all_artist(self):
    
    response = self.client.get(self.url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_search_one_artist(self):
    type_artist, _ = TypeOfFile.objects.get_or_create(**TypeOfFileFactory().build_type_of_file_JSON('artist'))
    artist, _ = Artist.objects.get_or_create(**ArtistFactory().build_artist_JSON(type_artist))
    
    response = self.client.get(self.url + str(artist.id) + '/')

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_search_artist_error(self):
    response = self.client.get(
      self.url + '/5324/',
      format='json'
    )

    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_new_artist(self):
    
    TypeOfFile.objects.get_or_create(**TypeOfFileFactory().build_type_of_file_JSON('artist'))

    artist ={
      "email": faker.email(),
      "name": faker.name(),
      "image": "",
      "nb_album": 0,
      "nb_fan": 0,
      "type": 1
    }

    response = self.client.post(
      self.url,
      artist,
      format='json'
    )

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Artist.objects.all().count(), 1)
    self.assertEqual(response.data['message'], 'Artista creado correctamente')

  def test_update_artist(self):

    type_artist, _ = TypeOfFile.objects.get_or_create(**TypeOfFileFactory().build_type_of_file_JSON('artist'))
    artist, _ = Artist.objects.get_or_create(**ArtistFactory().build_artist_JSON(type_artist))

    new_data ={
      "name": artist.name,
      "image": "https://www.google.com/image",
      "nb_fan": 1,
    }

    response = self.client.put(
      self.url + str(artist.id) + '/',
      new_data,
      format='json'
    )

    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  def test_delete_artist(self):

    type_artist, _ = TypeOfFile.objects.get_or_create(**TypeOfFileFactory().build_type_of_file_JSON('artist'))
    artist, _ = Artist.objects.get_or_create(**ArtistFactory().build_artist_JSON(type_artist))

    response = self.client.delete(
      self.url + str(artist.id) + '/',
      format='json'
    )

    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
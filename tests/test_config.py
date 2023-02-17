from faker import Faker

from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User

class TestSetUp(APITestCase):

  def setUp(self):

    faker = Faker()

    self.login_url = '/auth/login/'
    self.user = User.objects.create_superuser(
      first_name='Developer',
      last_name='Developer',
      username=faker.name(),
      password='developer',
      email=faker.email()
    )
    
    response = self.client.post(
      self.login_url,
      {
          'email': self.user.email,
          'password': 'developer'
      },
      format='json'
    )

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.token = response.data['tokens']['access']
    self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
    return super().setUp()   
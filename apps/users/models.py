from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):

  def _create_user(self, username, email, first_name,last_name, password, is_staff, is_superuser, **extra_fields):
    user = self.model(
      username = username,
      email = self.normalize_email(email),
      first_name = first_name,
      last_name = last_name,
      is_staff = is_staff,
      is_superuser = is_superuser,
      **extra_fields
    )
    user.set_password(password)
    user.save()
    return user

  def create_user(self, username, email, first_name,last_name, password=None, **extra_fields):
    return self._create_user(username, email, first_name,last_name, password, False, False, **extra_fields)

  def create_superuser(self, username, email, first_name,last_name, password=None, **extra_fields):
    return self._create_user(username, email, first_name,last_name, password, True, True, **extra_fields)


class User(AbstractUser, PermissionsMixin):
  # id = models.AutoField(primary_key=True)
  username = models.CharField(max_length=50, unique = True)
  email = models.EmailField('Correo Electrónico', max_length=100, unique=True, default="no@email.com")
  first_name = models.CharField('Nombres', max_length=50, null=True, blank = True)
  last_name = models.CharField('Apellidos', max_length=50, null=True, blank = True)
  image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
  date_of_birth = models.DateField('Fecha de cumpleaños',null=True)
  is_active = models.BooleanField(default = True)
  is_staff = models.BooleanField(default = False)
  is_superuser = models.BooleanField(default = False)

  objects = CustomUserManager()

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["username", "first_name", "last_name"]

  def __str__(self):
    return self.username
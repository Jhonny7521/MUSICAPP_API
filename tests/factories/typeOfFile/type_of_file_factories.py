from faker import Faker

from apps.songs.models.artist_model import Artist
from apps.songs.models.type_of_file_model import TypeOfFile
from apps.songs.api.serializers.type_of_file_serializer import TypeOfFileSerializer

faker = Faker()

class TypeOfFileFactory:

  def build_type_of_file_JSON(self, type):
    return {
      'name': type
    }

  def create_type_of_file(self, type):
    typeOfFile, _ = TypeOfFile.objects.get_or_create(**self.build_type_of_file_JSON(type))
    return typeOfFile

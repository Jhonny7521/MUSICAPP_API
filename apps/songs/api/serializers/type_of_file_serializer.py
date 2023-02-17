from rest_framework import serializers

from apps.songs.models.type_of_file_model import TypeOfFile

class TypeOfFileSerializer(serializers.ModelSerializer):

  class Meta:
    model = TypeOfFile
    fields = '__all__'

  def to_representation(self, instance):
    return {
      'id': instance.id,
      'name': instance.name
    }
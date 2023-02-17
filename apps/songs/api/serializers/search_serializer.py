from rest_framework import serializers

from apps.songs.models.tracks_model import Track

class SearchSerializer(serializers.ModelSerializer):

  class Meta:
    model = Track
    fields = '__all__'
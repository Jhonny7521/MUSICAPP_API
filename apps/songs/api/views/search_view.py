from urllib.parse import unquote

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.songs.models import Track, Artist
from apps.songs.api.serializers import SearchSerializer, TrackSerializer

class SearchViewSet(viewsets.ReadOnlyModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = SearchSerializer

  def list(self, request):
    query = request.query_params.get('q', None)

    if query:
      query = unquote(query)
      artist = Artist.objects.filter(name=query).first()

      if artist is not None:
        tracks = Track.objects.filter(artist=artist)
        serializer = self.serializer_class(tracks, many=True)

        response = {
          "data": serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)

      else:

        response = { 
          "error": "No existe el artista"
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    else:

      response = {
        "error": "Se requiere un parámetro 'q'"
      }

      return Response(response, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.songs.models import Artist
from apps.songs.api.serializers import ArtistSerializer

class ArtistViewSet(viewsets.ModelViewSet):
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer
  permission_classes = [IsAuthenticated]

  def create(self, request):
    serializer = ArtistSerializer(data=request.data)
    if isinstance(request.data, list):
      serializer = ArtistSerializer(data=request.data, many= True)
    
    if serializer.is_valid():
      serializer.save()
      response = {
        "message": "Artista creado correctamente", 
        "artist": serializer.data
      }

      return Response(response, status=status.HTTP_201_CREATED)

    response = {
      "message": "", 
      "error": serializer.errors
    }

    return Response(response, status=status.HTTP_400_BAD_REQUEST)
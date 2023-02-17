from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.songs.api.serializers import AlbumSerializer
from apps.songs.models import Album

class AlbumViewSet(viewsets.ModelViewSet):
  queryset = Album.objects.all()
  serializer_class = AlbumSerializer
  permission_classes = [IsAuthenticated]

  def create(self, request):
    serializer = AlbumSerializer(data=request.data)
    if isinstance(request.data, list):
      serializer = AlbumSerializer(data=request.data, many= True)
    
    if serializer.is_valid():
      serializer.save()
      response = {
        "message": "Álbum creado correctamente", 
        "album": serializer.data
      }

      return Response(response, status=status.HTTP_201_CREATED)

    response = {
      "message": "", 
      "error": serializer.errors
    }

    return Response(response, status=status.HTTP_400_BAD_REQUEST)
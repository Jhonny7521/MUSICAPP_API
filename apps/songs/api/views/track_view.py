from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.songs.models import Track
from apps.songs.api.serializers import TrackSerializer

class TrackViewSet(viewsets.ModelViewSet):
  queryset = Track.objects.all()
  serializer_class = TrackSerializer
  permission_classes = [IsAuthenticated]

  def create(self, request):

    serializer = TrackSerializer(data=request.data)
    if isinstance(request.data, list):
      serializer = TrackSerializer(data=request.data, many= True)
    
    
    if serializer.is_valid():
      serializer.save()
      response = {
        "message": "Pista creada correctamente", 
        "Track": serializer.data
      }

      return Response(response, status=status.HTTP_201_CREATED)

    response = {
      "message": "", 
      "error": serializer.errors
    }

    return Response(response, status=status.HTTP_400_BAD_REQUEST)
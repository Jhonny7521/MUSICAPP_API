from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.songs.models import TypeOfFile
from apps.songs.api.serializers import TypeOfFileSerializer

class TypeOfFileViewSet(viewsets.ModelViewSet):
  queryset = TypeOfFile.objects.all()
  serializer_class = TypeOfFileSerializer
  permission_classes = [IsAuthenticated]

  def create(self, request):
    serializer = TypeOfFileSerializer(data=request.data)
    if isinstance(request.data, list):
      serializer = TypeOfFileSerializer(data=request.data, many= True)
    
    if serializer.is_valid():
      file_type=serializer.save()
      print(file_type)
      response = {
        "message": "Creado correctamente", 
        "file_type": serializer.data
      }

      return Response(response, status=status.HTTP_201_CREATED)

    response = {
      "message": "", 
      "error": serializer.errors
    }

    return Response(response, status=status.HTTP_400_BAD_REQUEST)
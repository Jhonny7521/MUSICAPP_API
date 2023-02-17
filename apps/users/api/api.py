from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SignUpSerializer, GetUserSerializer
from apps.users.tokens import create_jwt_pair_for_user
from apps.users.models import User

# Create your views here.

class SignUpView(generics.GenericAPIView):
  serializer_class = SignUpSerializer

  def post(self, request: Request):
    data = request.data
    serializer = self.serializer_class(data=data)

    if serializer.is_valid():      
      serializer.save()
      # user = User.objects.filter(email=data.get('email')).first() # 1ra forma
      user = User.objects.filter(email=serializer.data.get('email')).first() # 2da forma
      tokens = create_jwt_pair_for_user(user)
      response = {"message": "El usuario se creó correctamente", "user_data": serializer.data, "tokens": tokens}
  
      return Response(data=response, status=status.HTTP_201_CREATED)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

  def post(self, request: Request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = authenticate(email=email, password=password)
    if user is not None:
      tokens = create_jwt_pair_for_user(user)
      idUser = User.objects.get(email=email)
      user_data = {
        'id': idUser.id,
        'username':idUser.username,
        'email':idUser.email,
        'is_superuser': idUser.is_superuser
      }
      # print(user_data)
      response = {"message": "Login exitoso", "user_data": user_data ,"tokens": tokens}

      return Response(data=response, status=status.HTTP_200_OK)

    else:
      return Response(data={"message": "Correo inválido o contraseña incorrecta"}, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request: Request):
      content = {"user": str(request.user), "auth": str(request.auth)}

      return Response(data=content, status=status.HTTP_200_OK)


class Logout(GenericAPIView):
  def post(self, request, *args, **kwargs):
    user = User.objects.filter(id=request.data.get('user', 0))
    if user.exists():
      RefreshToken.for_user(user.first())
      return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
    return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)

class GetUsers(viewsets.ReadOnlyModelViewSet):
  serializer_class = GetUserSerializer
  queryset = User.objects.all()

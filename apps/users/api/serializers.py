from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from django.contrib.auth import get_user_model
from apps.users.models import User

class SignUpSerializer(serializers.ModelSerializer):
  first_name = serializers.CharField(max_length=50)
  last_name = serializers.CharField(max_length=50)
  email = serializers.EmailField(max_length=80)
  username = serializers.CharField(max_length=45)
  password = serializers.CharField(min_length=8, write_only=True)

  class Meta:
    model = User
    fields = ["first_name", "last_name", "email", "username", "password"]

  def validate_email(self, value):
    if User.objects.filter(email=value).exists():
      raise ValidationError("El email ya ha sido usado")
    return value

  def create(self, validated_data):
    password = validated_data.pop("password")
    user = super().create(validated_data)
    user.set_password(password)
    user.save()

    return user


class GetUserSerializer(serializers.ModelSerializer):
  email = serializers.CharField(max_length=80)
  username = serializers.CharField(max_length=45)
  password = serializers.CharField(min_length=8, write_only=True)

  class Meta:
    model = User
    fields = ["email", "username", "password"]   
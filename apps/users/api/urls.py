from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .api import LoginView, SignUpView

urlpatterns = [
  path("signup/", SignUpView.as_view(), name="signup"),
  path("login/", LoginView.as_view(), name="login"),
  path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
  path("jwt/refresh/", TokenRefreshView.as_view(), name="tokoen_refresh"),
]

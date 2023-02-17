from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Vista general e información de la API
schema_view = get_schema_view(
   openapi.Info(
      title="MUSICAPP API",
      default_version='v1',
      description="Proyecto MUSICAPP API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jhonny.jql1210@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.users.api.urls')),
    path('', include('apps.songs.api.routers')),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

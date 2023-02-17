from apps.songs.api.views.album_view import AlbumViewSet
from apps.songs.api.views.artist_view import ArtistViewSet
from apps.songs.api.views.track_view import TrackViewSet
from apps.songs.api.views.type_of_file_view import TypeOfFileViewSet

from apps.songs.api.views.search_view import SearchViewSet

"""
Esta es la estructura completa de mi proyecto

root_folder/
  __init__.py
  asgi.py
  settings.py
  urls.py
  wsgi.py

apps/
  songs/ 
    api/
      serializers/
        __init__.py
        album_serializer.py
        artist_serializer.py
        track_serilizer.py
        type_of_file_serilizer.py

      viewsets/
        __init__.py
        album_viewset.py
        artist_viewset.py
        track_viewset.py
        type_of_file_viewset.py

    models/
      __init__.py
      album_model.py
      artist_model.py
      track_model.py
      type_of_file_model.py

    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py

manage.py

como podría hacer las migraciones de mi aplicacion songs
"""

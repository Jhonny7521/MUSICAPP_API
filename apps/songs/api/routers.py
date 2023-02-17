from rest_framework.routers import DefaultRouter

from apps.songs.api.views import ( AlbumViewSet, ArtistViewSet, TrackViewSet,
                                  TypeOfFileViewSet, SearchViewSet )

songs_router = DefaultRouter()

songs_router.register(r'album', AlbumViewSet, basename='albums')
songs_router.register(r'artist', ArtistViewSet, basename='artist')
songs_router.register(r'tracks', TrackViewSet, basename='tracks')
songs_router.register(r'fileTypes', TypeOfFileViewSet, basename='fileTypes')
songs_router.register(r'search', SearchViewSet, basename='fileTypes')


urlpatterns = songs_router.urls
from django.urls import path
from .views import (
    SongListCreateView,
    SongRetrieveUpdateDestroyView,
    SpotifySearchView,
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
    export_songs,
    get_favorite_songs, 
    import_songs,
    toggle_favorite_song
)

urlpatterns = [
    path('songs/', SongListCreateView.as_view(), name="song-list"),
    path('songs/<int:pk>/', SongRetrieveUpdateDestroyView.as_view(), name="song-detail"),
    path('songs/export/', export_songs, name='export_songs'),
    path('songs/import/', import_songs, name='import_songs'),
    path('songs/favorite/', toggle_favorite_song, name='toggle_favorite_song'),
    path('songs/favorites/', get_favorite_songs, name='get_favorite_songs'),
    path('users/', UserListCreateView.as_view(), name="user-list"),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name="user-detail"),
    path('spotify/search/', SpotifySearchView.as_view(), name="spotify-search"),
]

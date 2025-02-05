from django.urls import path
from .views import (
    SongListCreateView,
    SongRetrieveUpdateDestroyView,
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('songs/', SongListCreateView.as_view(), name="song-list"),
    path('songs/<int:pk>/', SongRetrieveUpdateDestroyView.as_view(), name="song-detail"),
    path('users/', UserListCreateView.as_view(), name="user-list"),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name="user-detail"),
]

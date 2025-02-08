import json
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.core.exceptions import ValidationError
from .utils import export_songs_to_json, import_songs_from_json
from .spotify import search_song
from .models import Song, User
from .serializers import SongSerializer, UserSerializer

class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class SongRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class SpotifySearchView(APIView):
    def get(self, request, *args, **kwargs):
        song_name = request.query_params.get("song")
        if not song_name:
            return Response({"error": "Necesitas añadir una canción"}, status=400)
        data = search_song(song_name)
        return Response(data)
    
@api_view(['GET'])
def export_songs(request):
    if not request.user.is_authenticated:
        return Response({"detail": "Error de autenticación."}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        response = export_songs_to_json()
        return response
    except ValidationError as e:
        return HttpResponse(f"Error: {str(e)}", status=400)

@api_view(['POST'])
def import_songs(request):
    if not request.user.is_authenticated:
        return Response({"detail": "Error de autenticación."}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        json_data = request.data

        if not json_data:
            return Response({"detail": "Necesitas proporcionar datos JSON."}, status=status.HTTP_400_BAD_REQUEST)

        import_songs_from_json(json.dumps(json_data))
        return Response({"detail": "¡Éxito! Canciones importadas"}, status=status.HTTP_200_OK)

    except ValidationError as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except json.JSONDecodeError:
        return Response({"detail": "El JSON enviado no es válido."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_favorite_song(request):
    title = request.data.get('title')
    artist = request.data.get('artist')

    if not title or not artist:
        return Response({"detail": "Debes proporcionar 'title' y 'artist'."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        song = Song.objects.get(title__iexact=title, artist__iexact=artist)
    except Song.DoesNotExist:
        return Response({"detail": "Canción no encontrada."}, status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if user.favorite_songs.filter(id=song.id).exists():
        user.favorite_songs.remove(song)
        user.save()
        return Response({"detail": "Canción eliminada de favoritos."}, status=status.HTTP_200_OK)
    else:
        user.favorite_songs.add(song)
        user.save()
        return Response({"detail": "Canción añadida a favoritos."}, status=status.HTTP_200_OK)

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_favorite_songs(request):
    favorite_songs = request.user.favorite_songs.all()
    songs_data = [{"id": song.id, "title": song.title, "artist": song.artist, "album": song.album} for song in favorite_songs]
    return Response(songs_data, status=status.HTTP_200_OK)
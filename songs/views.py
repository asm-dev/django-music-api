from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .spotify import search_song
from .models import Song, User
from .serializers import SongSerializer, UserSerializer

class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]

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
            return Response({"error": "Se requiere el parámetro 'song'"}, status=400)
        data = search_song(song_name)
        return Response(data)
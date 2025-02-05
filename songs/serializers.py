from rest_framework import serializers
from .models import Song, User

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album']

class UserSerializer(serializers.ModelSerializer):
    favorite_songs = serializers.PrimaryKeyRelatedField(
        queryset=Song.objects.all(), many=True, required=False
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'favorite_songs']

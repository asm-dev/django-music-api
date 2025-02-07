from rest_framework import serializers
from .models import Song, User

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El título debe tener al menos 5 caracteres.")
        return value
    
    def validate_artist(self, value):
        if not value.strip():
            raise serializers.ValidationError("La canción ha de tener un artista asociado.")
        return value

    def validate_duplication(self, value):
        title = value.get('title')
        artist = value.get('artist')

        if Song.objects.filter(title__iexact=title, artist__iexact=artist).exists():
            raise serializers.ValidationError("No puedes agregar canciones que ya existan.")
        return value

class UserSerializer(serializers.ModelSerializer):
    favorite_songs = serializers.PrimaryKeyRelatedField(
        queryset=Song.objects.all(), many=True, required=False
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'favorite_songs']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo ya está registrado.")
        return value
    
    def validate_favorite_songs(self, value):
        validated_songs = []
        
        for song in value:
            existing_song = Song.objects.filter(title__iexact=song.title, artist__iexact=song.artist).first()
            
            if not existing_song:
                existing_song = Song.objects.create(title=song.title, artist=song.artist, album=song.album)

            if existing_song not in validated_songs:
                validated_songs.append(existing_song)
        
        return validated_songs
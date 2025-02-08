import json
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from .models import Song

def export_songs_to_json():
    songs = Song.objects.all()
    songs_data = [
        {'title': song.title, 'artist': song.artist, 'album': song.album} for song in songs
    ]
    response_data = json.dumps(songs_data, ensure_ascii=False, indent=4)
    response = HttpResponse(response_data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="songs_export.json"'
    return response

def import_songs_from_json(json_data):
    try:
        songs = json.loads(json_data)
        for song in songs:
            if Song.objects.filter(title__iexact=song['title'], artist__iexact=song['artist']).exists():
                raise ValidationError(f"La canción {song['title']} de {song['artist']} ya existe.")
            Song.objects.create(title=song['title'], artist=song['artist'], album=song.get('album', ''))
    except json.JSONDecodeError:
        raise ValidationError("El archivo JSON no es válido.")

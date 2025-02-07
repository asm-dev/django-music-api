import json
from .models import Song

def export_songs():
    songs = list(Song.objects.values())
    with open('songs.json', 'w') as f:
        json.dump(songs, f)

def import_songs():
    with open('songs.json', 'r') as f:
        songs = json.load(f)
        for song in songs:
            Song.objects.create(**song)

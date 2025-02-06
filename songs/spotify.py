import requests
from django.conf import settings

SPOTIFY_CLIENT_ID = 'mover a env'
SPOTIFY_CLIENT_SECRET = 'mover a env'

def get_spotify_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": SPOTIFY_CLIENT_ID,
        "client_secret": SPOTIFY_CLIENT_SECRET
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token")

def search_song(song_name):
    token = get_spotify_token()
    url = f"https://api.spotify.com/v1/search?q={song_name}&type=track"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()

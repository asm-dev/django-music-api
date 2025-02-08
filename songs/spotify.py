import requests
import os
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

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
    url = f"https://api.spotify.com/v1/search?q={quote(song_name)}&type=track"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return {"error": "No se pudo conectar a Spotify"}
    
    data = response.json()
    tracks = data.get("tracks", {}).get("items", [])
    
    results = []
    for track in tracks:
        results.append({
            "title": track["name"],
            "artist": ", ".join(artist["name"] for artist in track["artists"]),
            "album": track["album"]["name"],
            "release_date": track["album"]["release_date"],
            "preview_url": track.get("preview_url", "No disponible"),
            "spotify_url": track["external_urls"]["spotify"],
        })
    
    return results

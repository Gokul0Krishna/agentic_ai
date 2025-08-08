import yt_dlp
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
from dotenv import load_dotenv
import spotipy.client
import spotipy.oauth2

def _safe_del(self):
    try:
        pass
    except Exception:
        pass

spotipy.client.Spotify.__del__ = _safe_del
spotipy.oauth2.SpotifyAuthBase.__del__ = _safe_del

clientid=os.getenv("clientid")

clientkey=os.getenv("clientsecret")

if not clientid or not clientkey:
    raise RuntimeError("Spotify credentials not found in environment. "
                       "Make sure 'clientid' and 'clientsecret' are set in your .env file.")


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=clientid,
    client_secret=clientkey,
))

# enter the url
lis={
    "songname":[],
    "artist":[]
}

playlist_url="https://open.spotify.com/playlist/1RGuytR83Dc7dw8C14aecB?si=082a4026ae3b42f4"
playlist_id = playlist_url.split("/")[-1].split("?")[0]

results = sp.playlist_items(playlist_id, additional_types=["track"])
while True:
    for item in results.get("items", []):
        track = item.get("track")
        if not track:
            continue  # skip if missing
        title = track.get("name", "Unknown Title")
        # join all artist names (track["artists"] is a list)
        artists = ", ".join(a.get("name", "") for a in track.get("artists", []))
        lis["songname"].append(title)
        lis["artist"].append(artists)
        # optional: inspect when it was added
    if results.get("next"):
        results = sp.next(results)
    else:
        break






for i in range(len(lis["songname"])):
    try:
        query = f"{lis['songname'][i]} {lis['artist'][i]}"
        ydl_opts = {
            "format": "bestaudio/best",
            "noplaylist": True,
            "cookies": r"C:\Users\ASUS\Downloads\www.youtube.com_cookies.txt",
            "outtmpl": os.path.join("C:/Users/ASUS/Music/workout", "%(title)s.%(ext)s"), 
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "default_search": "ytsearch1",  # search and take top result
             "socket_timeout": 60,
            # retry on transient errors
            "retries": 10,
            "retry_sleep_functions": "lambda attempts: min(10, attempts)",  # backoff
            "abort_on_unavailable_fragment": True,  # try to continue even if one piece fails
            "continuedl": True,  # resume partially downloaded files
            "quiet": False,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([query])
    except Exception:
        pass

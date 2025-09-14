import random
from typing import Dict, Optional

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from src.config import config


class SpotifyService:
    def __init__(self):
        client_credentials_manager = SpotifyClientCredentials(
            client_id=config.SPOTIFY_CLIENT_ID,
            client_secret=config.SPOTIFY_CLIENT_SECRET,
        )
        self.spotify = spotipy.Spotify(
            client_credentials_manager=client_credentials_manager
        )

    def get_random_track_from_playlist(self) -> Optional[Dict]:
        """Fetches a random song from the Twenty One Pilots playlist"""
        try:
            # First call to get playlist information
            playlist_info = self.spotify.playlist(config.SPOTIFY_PLAYLIST_ID)
            total_tracks = playlist_info["tracks"]["total"]

            # Choose a random offset
            random_offset = random.randint(0, max(0, total_tracks - 1))

            # Fetch a song at the random offset
            results = self.spotify.playlist_tracks(
                config.SPOTIFY_PLAYLIST_ID,
                offset=random_offset,
                limit=1,
            )

            if results["items"] and results["items"][0]["track"]:
                track = results["items"][0]["track"]

                return {
                    "id": track["id"],
                    "name": track["name"],
                    "artist": ", ".join(
                        [artist["name"] for artist in track["artists"]]
                    ),
                    "album": track["album"]["name"],
                    "release_date": track["album"]["release_date"],
                    "preview_url": track["preview_url"],
                    "spotify_url": track["external_urls"]["spotify"],
                    "image_url": track["album"]["images"][0]["url"]
                    if track["album"]["images"]
                    else None,
                }

        except Exception as e:
            print(f"-> error searching for song on Spotify: {e}")
            return None

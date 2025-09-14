import asyncio
import sys

from src.discord_service import DiscordService
from src.spotify_service import SpotifyService


async def main():
    """Main function of the Sahlo Folina bot"""

    print("Starting Sahlo Folina...")

    spotify_service = SpotifyService()
    discord_service = DiscordService()

    try:
        print("-> searching for random song on Spotify...")
        track = spotify_service.get_random_track_from_playlist()

        if not track:
            print("-> could not get song from Spotify")
            sys.exit(1)

        print(f"-> selected song: {track['name']} - {track['artist']}")
        print(f"-> album: {track['album']}")

        print("-> sending to Discord...")
        success = await discord_service.send_daily_song(track)

        if success:
            print("-> Sahlo Folina executed successfully!")
            print(f"-> song of the day: {track['name']}")
        else:
            print("-> error sending to Discord")
            sys.exit(1)

    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())

from http import HTTPStatus
from typing import Dict

import aiohttp

from src.config import config


class DiscordService:
    def __init__(self):
        self.webhook_url = config.DISCORD_WEBHOOK_URL

    async def send_daily_song(self, track_data: Dict) -> bool:
        """Sends the daily song to the Discord channel via webhook"""

        if not self.webhook_url:
            print("❌ DISCORD_WEBHOOK_URL not configured!")
            return False

        # Create embed
        embed = {
            "title": "Sahlo Folina - Song of the Day",
            "description": f"**{track_data['name']}**\n*{track_data['album']}* • {track_data.get('release_date', 'N/A')[:4] if track_data.get('release_date') else 'N/A'}\n\n[Listen on Spotify]({track_data['spotify_url']})",
            "color": 0xFF0000,
            "footer": {
                "text": "Twenty One Pilots Daily Song • FPE |-/",
                "icon_url": "https://i.scdn.co/image/ab6761610000e5eb196972172c81d18b7db34d9e",
            },
        }

        # Add album image
        if track_data.get("image_url"):
            embed["thumbnail"] = {"url": track_data["image_url"]}

        # Webhook payload
        payload = {"embeds": [embed]}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.webhook_url, json=payload
                ) as response:
                    if response.status == HTTPStatus.NO_CONTENT:
                        print("-> Message sent successfully!")
                        return True
                    else:
                        print(f"-> Error: HTTP {response.status}")
                        error_text = await response.text()
                        print(f"-> err: {error_text}")
                        return False

        except Exception as e:
            print(f"-> Error sending webhook: {e}")
            return False

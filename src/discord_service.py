from http import HTTPStatus
from typing import Dict

import aiohttp

from config import config


class DiscordService:
    def __init__(self):
        self.webhook_url = config.DISCORD_WEBHOOK_URL

    async def send_daily_song(self, track_data: Dict, analysis: str) -> bool:
        """Envia a música diária para o canal do Discord via webhook"""

        if not self.webhook_url:
            print("❌ DISCORD_WEBHOOK_URL não configurada!")
            return False

        # Criar embed
        embed = {
            "title": "Sahlo Folina - Música do Dia",
            "description": f"**{track_data['name']}**\n*{track_data['album']}* • {track_data['release_date'][:4]}\n\n[Ouvir no Spotify]({track_data['spotify_url']})",
            "color": 0xFF0000,
            "fields": [
                {
                    "name": "Sobre a música",
                    "value": analysis,
                    "inline": False,
                }
            ],
            "footer": {
                "text": "Twenty One Pilots Daily Song • FPE |-/",
                "icon_url": "https://i.scdn.co/image/ab6761610000e5eb196972172c81d18b7db34d9e",
            },
        }

        # Adicionar imagem do álbum
        if track_data.get("image_url"):
            embed["thumbnail"] = {"url": track_data["image_url"]}

        # Payload do webhook
        payload = {"embeds": [embed]}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.webhook_url, json=payload
                ) as response:
                    if response.status == HTTPStatus.NO_CONTENT:
                        print("-> Mensagem enviada com sucesso!")
                        return True
                    else:
                        print(f"-> Erro: HTTP {response.status}")
                        error_text = await response.text()
                        print(f"-> err: {error_text}")
                        return False

        except Exception as e:
            print(f"-> Erro ao enviar webhook: {e}")
            return False

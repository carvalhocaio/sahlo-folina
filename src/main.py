import asyncio
import sys
from datetime import datetime

from src.anthropic_service import AnthropicService
from src.discord_service import DiscordService
from src.spotify_service import SpotifyService


async def main():
    """Função principal do bot Sahlo Folina"""

    print("Iniciando Sahlo Folina...")
    print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 30)

    # Inicializar serviços
    spotify_service = SpotifyService()
    anthropic_service = AnthropicService()
    discord_service = DiscordService()

    try:
        print("-> buscando música aleatória no Spotify...")
        track = spotify_service.get_random_track_from_playlist()

        if not track:
            print("-> não foi possível obter música do Spotify")
            sys.exit(1)

        print(f"-> música selecionada: {track['name']} - {track['artist']}")
        print(f"-> álbum: {track['album']}")

        print("-> gerando análise com Claude...")
        analysis = anthropic_service.generate_song_analysis(
            track["name"],
            track["artist"],
            track["album"],
        )

        if not analysis:
            print("-> não foi possível gerar análise")
            sys.exit(1)

        print("-> análise gerada com sucesso")

        print("-> enviando para Discord...")
        success = await discord_service.send_daily_song(track, analysis)

        if success:
            print("-> Sahlo Folina executado com sucesso!")
            print(f"-> música do dia: {track['name']}")
        else:
            print("-> erro ao enviar para Discord")
            sys.exit(1)

    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())

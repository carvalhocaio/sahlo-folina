from typing import Optional

import anthropic

from src.config import config


class AnthropicService:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)

    def generate_song_analysis(
        self, song_name: str, artist: str, album: str
    ) -> Optional[str]:
        """Gera análise sobre a música usando Anthropic Claude"""

        prompt = f"""
        Escreva uma análise concisa sobre a música "{song_name}" do Twenty One Pilots, do álbum "{album}".

        IMPORTANTE: Limite sua resposta a no máximo 900 caracteres.

        Inclua 2-3 dos seguintes tópicos:
        - Contexto na discografia da banda
        - Seu impacto na lore da banda (se for o caso)
        - Temas principais da letra (sem reproduzir letras completas)
        - Estilo musical e elementos de produção interessantes
        - Curiosidades sobre a criação ou significado da música
        - Por que essa música é especial para os fãs do Twenty One Pilots

        Use tom casual para comunidade Discord. Não use emojis.
        Se não conhecer a música, mencione que é um lançamento recente.
        Termine com "|-/"
        """

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=250,
                messages=[{"role": "user", "content": prompt}],
            )

            return response.content[0].text.strip()

        except Exception as e:
            print(f"Erro ao gerar análise: {e}")
            return f"-> Hoje a música escolhida é **{song_name}** do álbum *{album}*! \n\n|-/"

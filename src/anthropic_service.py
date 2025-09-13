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
        Escreva uma análise interessante e envolvente sobre a música "{song_name}"
        do Twenty One Pilots, do álbum "{album}".

        Inclua:
        - Contexto da música dentro da discografia da banda
        - Seu impacto na lore da banda (se for o caso)
        - Temas principais abordados na letra (sem reproduzir letras completas)
        - Estilo musical e elementos de produção interessantes
        - Curiosidades sobre a criação ou significado da música
        - Por que essa música é especial para os fãs do Twenty One Pilots

        Mantenha um tom casual e informativo, como se fosse para uma comunidade
        de fãs no Discord. Não use emojis.

        Caso não encontre a letra da música, é porque provavelmente a música
        é nova, tente procurar em outras fontes, caso não encontre, retorne
        que a música é lançamento e que não foi possível fazer uma análise.

        Garanto que é uma música oficial do Twenty One Pilots.

        Termine sempre com "|-/" (o símbolo oficial da banda).
        """

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}],
            )

            return response.content[0].text.strip()

        except Exception as e:
            print(f"Erro ao gerar análise: {e}")
            return f"-> Hoje a música escolhida é **{song_name}** do álbum *{album}*! \n\n|-/"

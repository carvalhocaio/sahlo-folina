# Sahlo Folina

Bot automatizado que seleciona músicas aleatórias do Twenty One Pilots de uma playlist no Spotify e envia para um canal do Discord via webhook.

## Objetivo

O **Sahlo Folina** é um projeto que conecta fãs do Twenty One Pilots através da música diária. O bot:

- Seleciona aleatoriamente uma música de uma playlist específica do Spotify
- Envia a música do dia para um canal do Discord com embed personalizado

## Funcionalidades

- **Seleção Aleatória**: Busca músicas aleatórias de playlist do Spotify
- **Integração Discord**: Envia embeds formatados para canais do Discord
- **Design Personalizado**: Visual temático do Twenty One Pilots
- **Links Diretos**: Links para Spotify

##  Estrutura do Projeto

```
sahlo-folina/
├── src/
│   ├── __init__.py             # Inicialização do pacote
│   ├── main.py                 # Arquivo principal
│   ├── config.py               # Configurações e variáveis de ambiente
│   ├── spotify_service.py      # Serviço de integração com Spotify
│   └── discord_service.py      # Serviço de webhook do Discord
├── .env.example                # Exemplo de variáveis de ambiente
├── requirements.txt            # Dependências do projeto
├── Makefile                    # Comandos de desenvolvimento
└── README.md                   # Este arquivo
```

## Dependências

### Requisitos do Sistema
- Python 3.12+
- Ambiente virtual Python

### Bibliotecas Python
- `spotipy==2.23.0` - Integração com Spotify Web API
- `python-dotenv==1.0.0` - Gerenciamento de variáveis de ambiente
- `aiohttp==3.9.1` - Cliente HTTP assíncrono para Discord webhooks

### APIs Necessárias
- **Spotify Web API** - Para acessar informações das músicas
- **Discord Webhook** - Para enviar mensagens para canais do Discord

## Configuração

### 1. Variáveis de Ambiente

Copie o arquivo `.env.example` para `.env`:

```bash
cp .env.example .env
```

Configure as seguintes variáveis:

```env
# Spotify API
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_PLAYLIST_ID=your_twenty_one_pilots_playlist_id

# Discord Webhook
DISCORD_WEBHOOK_URL=your_discord_webhook_url
```

### 2. Como Obter as Credenciais

#### Spotify API
1. Acesse [Spotify for Developers](https://developer.spotify.com/)
2. Crie um novo app
3. Copie o Client ID e Client Secret
4. Para o Playlist ID, use o ID da playlist do Twenty One Pilots

#### Discord Webhook
1. No seu servidor Discord, vá em Configurações do Canal
2. Integrações > Webhooks > Novo Webhook
3. Copie a URL do webhook

## Instalação e Execução

### 1. Clone o Repositório
```bash
git clone <url-do-repositorio>
cd sahlo-folina
```

### 2. Configure o Ambiente Virtual
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows
```

### 3. Instale as Dependências
```bash
# Com uv (recomendado)
uv pip install -r requirements.txt

# Ou com pip tradicional
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente
Edite o arquivo `.env` com suas credenciais (veja seção de Configuração).

### 5. Execute o Bot
```bash
# Ative o ambiente virtual
source .venv/bin/activate

# Execute o bot
python src/main.py

# Ou usando o Makefile
make run
```

## Desenvolvimento

### Comandos Disponíveis (Makefile)

```bash
# Executar o projeto
make run

# Verificar código (linting)
make lint

# Formatar código automaticamente
make format
```

### Formatação e Linting

O projeto usa **Ruff** para formatação e linting do código Python:

- Configuração em `ruff.toml`
- Executar verificações: `make lint`
- Formatação automática: `make format`

### Estrutura de Código

- **Modular**: Cada serviço (Spotify, Discord) em arquivo separado
- **Async/Await**: Operações assíncronas para melhor performance
- **Type Hints**: Tipagem Python para melhor documentação
- **Error Handling**: Tratamento de erros em todas as operações

## Como Usar

1. Configure todas as variáveis de ambiente
2. Execute o bot: `python src/main.py`
3. O bot irá:
  - Buscar uma música aleatória da playlist
  - Enviar para o Discord com embed formatado

## Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/:name`)
3. Faça commit das mudanças (`git commit -m 'Add some feature'`)
4. Push para a branch (`git push origin feature/:name`)
5. Abra um Pull Request


---

**FPE |-/**

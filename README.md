# Sahlo Folina

Automated bot that selects random Twenty One Pilots songs from a Spotify playlist and sends them to a Discord channel via webhook.

## Purpose

**Sahlo Folina** is a project that connects Twenty One Pilots fans through daily music. The bot:

- Randomly selects a song from a specific Spotify playlist
- Sends the song of the day to a Discord channel with a custom embed

## Features

- **Random Selection**: Fetches random songs from Spotify playlist
- **Discord Integration**: Sends formatted embeds to Discord channels
- **Custom Design**: Twenty One Pilots themed visuals
- **Direct Links**: Links to Spotify

## Project Structure

```
sahlo-folina/
├── src/
│   ├── __init__.py             # Package initialization
│   ├── main.py                 # Main file
│   ├── config.py               # Configuration and environment variables
│   ├── spotify_service.py      # Spotify integration service
│   └── discord_service.py      # Discord webhook service
├── .env.example                # Environment variables example
├── requirements.txt            # Project dependencies
├── Makefile                    # Development commands
└── README.md                   # This file
```

## Dependencies

### System Requirements
- Python 3.12+
- Python virtual environment

### Python Libraries
- `spotipy==2.23.0` - Spotify Web API integration
- `python-dotenv==1.0.0` - Environment variables management
- `aiohttp==3.9.1` - Asynchronous HTTP client for Discord webhooks

### Required APIs
- **Spotify Web API** - To access song information
- **Discord Webhook** - To send messages to Discord channels

## Configuration

### 1. Environment Variables

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

Configure the following variables:

```env
# Spotify API
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_PLAYLIST_ID=your_twenty_one_pilots_playlist_id

# Discord Webhook
DISCORD_WEBHOOK_URL=your_discord_webhook_url
```

### 2. How to Obtain Credentials

#### Spotify API
1. Go to [Spotify for Developers](https://developer.spotify.com/)
2. Create a new app
3. Copy the Client ID and Client Secret
4. For the Playlist ID, use the Twenty One Pilots playlist ID

#### Discord Webhook
1. In your Discord server, go to Channel Settings
2. Integrations > Webhooks > New Webhook
3. Copy the webhook URL

## Installation and Execution

### 1. Clone the Repository
```bash
git clone <repository-url>
cd sahlo-folina
```

### 2. Set up Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
# With uv (recommended)
uv pip install -r requirements.txt

# Or with traditional pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Edit the `.env` file with your credentials (see Configuration section).

### 5. Run the Bot
```bash
# Activate virtual environment
source .venv/bin/activate

# Run the bot
python src/main.py

# Or using Makefile
make run
```

## Development

### Available Commands (Makefile)

```bash
# Run the project
make run

# Check code (linting)
make lint

# Format code automatically
make format
```

### Formatting and Linting

The project uses **Ruff** for Python code formatting and linting:

- Configuration in `ruff.toml`
- Run checks: `make lint`
- Automatic formatting: `make format`

### Code Structure

- **Modular**: Each service (Spotify, Discord) in separate files
- **Async/Await**: Asynchronous operations for better performance
- **Type Hints**: Python typing for better documentation
- **Error Handling**: Error handling in all operations

## How to Use

1. Configure all environment variables
2. Run the bot: `python src/main.py`
3. The bot will:
  - Fetch a random song from the playlist
  - Send it to Discord with formatted embed

## Contributing

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/:name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/:name`)
5. Open a Pull Request


---

**FPE |-/**

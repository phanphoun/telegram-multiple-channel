# Telegram Multiple Channel Bridge Bot

A Telegram bot that automatically forwards messages from multiple channels to a discussion group and adds a "Join Discussion" button to the original posts.

## Features

- **Multi-channel support**: Watch multiple Telegram channels simultaneously
- **Automatic forwarding**: Forwards new messages from channels to a designated discussion group
- **Discussion links**: Generates direct links to the forwarded messages in the discussion group
- **Interactive buttons**: Adds a "💬 Join Discussion" button to original channel posts for easy navigation

## Prerequisites

- Python 3.7 or higher
- Telegram API credentials (API ID and API Hash)
- Telegram Bot Token

## Installation

1. Clone the repository:
```bash
git clone https://github.com/phanphoun/telegram-multiple-channel.git
cd telegram-multiple-channel
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Edit `app.py` and update the following configuration values:

```python
# Your Telegram API credentials (get from https://my.telegram.org)
API_ID = 'your_api_id'
API_HASH = 'your_api_hash'

# Your bot token (get from @BotFather)
BOT_TOKEN = 'your_bot_token'

# List of channel usernames to monitor
CHANNELS = ['channel1', 'channel2', 'channel3']

# Target discussion group username
TARGET_GROUP = 'discussion_group'
```

### Getting API Credentials

1. **API ID and API Hash**:
   - Go to https://my.telegram.org
   - Sign in with your phone number
   - Navigate to "API development tools"
   - Create a new application to get your API ID and API Hash

2. **Bot Token**:
   - Start a chat with @BotFather on Telegram
   - Send `/newbot` and follow the instructions
   - Copy the bot token provided

## Bot Permissions

The bot must have the following permissions:
- **In channels**: "Edit Messages" permission to add buttons to posts
- **In discussion group**: Must be a member to forward messages

## Usage

Run the bot:
```bash
python app.py
```

The bot will start monitoring the configured channels and automatically:
1. Forward new messages to the discussion group
2. Generate a discussion link
3. Add a "💬 Join Discussion" button to the original post

## How It Works

1. When a new message is posted in any monitored channel
2. The bot forwards it to the designated discussion group
3. A direct link to the forwarded message is created
4. The bot edits the original channel post to add a button that links to the discussion

## Troubleshooting

- **Bot doesn't forward messages**: Ensure the bot is a member of the discussion group
- **Button not added**: Verify the bot has "Edit Messages" permission in the channels
- **API errors**: Check that your API credentials and bot token are correct

## License

MIT License

## Contributing

Feel free to submit issues and pull requests.

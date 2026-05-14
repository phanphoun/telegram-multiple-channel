from telethon import TelegramClient, events, Button
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# --- CONFIGURATION ---
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Channels to watch and the group where the discussion happens
CHANNELS = os.getenv('CHANNELS', '').split(',')
TARGET_GROUP = os.getenv('TARGET_GROUP') # The username of your group

client = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(chats=CHANNELS))
async def handle_new_post(event):
    try:
        print(f"📩 New message received from: {event.chat_id} ({event.chat.title if hasattr(event.chat, 'title') else 'N/A'})")
        print(f"   Message ID: {event.id}")
        
        # 1. Forward the message to the discussion group
        # This returns the message object sent to the group
        print(f"   Attempting to forward to: {TARGET_GROUP}")
        forwarded = await client.forward_messages(TARGET_GROUP, event.message)
        print(f"   ✅ Forwarded successfully! New message ID: {forwarded.id}")
        
        # 2. Create the link to that specific message in the group
        # This link allows users to jump directly to the discussion
        discussion_link = f"https://t.me/{TARGET_GROUP}/{forwarded.id}"
        print(f"   Discussion link: {discussion_link}")
        
        # 3. Add a "💬 Join Discussion" button to the original channel post
        # The bot must have "Edit Messages" permission in the channel
        print(f"   Adding button to original message...")
        await client.edit_message(
            event.chat_id, 
            event.id, 
            buttons=Button.url("💬 Join Discussion", discussion_link)
        )
        print(f"   ✅ Button added successfully!")
        
        print(f"✅ Complete: Forwarded and added button for: {event.chat.title}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

print("Professional Bridge Bot is running...")
client.run_until_disconnected()

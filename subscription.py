from telethon.sync import TelegramClient
from bot.config import API_ID, API_HASH, CHANNEL_ID

client = TelegramClient("session_name", API_ID, API_HASH)

async def check_subscription(user_id):
    """Checks if user is already in the private channel"""
    async with client:
        try:
            participants = await client.get_participants(CHANNEL_ID, aggressive=True)
            return any(user.id == user_id for user in participants)
        except Exception as e:
            print(f"Error checking subscription: {e}")
            return False

async def add_user_to_channel(user_id):
    """Adds user to the private channel"""
    async with client:
        try:
            await client(telethon.functions.channels.InviteToChannelRequest(CHANNEL_ID, [user_id]))
            return True
        except Exception as e:
            print(f"Error adding user to channel: {e}")
            return False

from dotenv import load_dotenv
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio

load_dotenv()


API_BOT_ID = os.getenv("API_BOT_ID")
API_BOT_HASH = os.getenv("API_BOT_HASH")
API_BOT_TOKEN = os.getenv("API_BOT_TOKEN")


session = StringSession()

client = TelegramClient(session, API_BOT_ID, API_BOT_HASH)


async def main(): 
    await client.start(bot_token=API_BOT_TOKEN)
    channels = ['testchannel32151', 'testchannel3214']
    message = "Test message"
    for channel in channels:
        await client.send_message(channel, message)


asyncio.run(main())

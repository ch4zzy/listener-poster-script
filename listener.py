from telethon import TelegramClient
from dotenv import load_dotenv
import os
import asyncio
import datetime
from telethon.sessions import StringSession


load_dotenv()


API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')


session = StringSession()

client = TelegramClient(session, API_ID, API_HASH)


async def main():
    await client.start()
    print(client.session.save())
    channels = ['testchannel32151', "DeepStateUA"]
    last_message_time = {channel: None for channel in channels}
    for channel in channels:
        async for message in client.iter_messages(channel, limit=1):
            print(f"Last message in {channel}: {message.message}, {message.date}")
            last_message_time[channel] = message.date
    
    await asyncio.sleep(5)

    while True:
        print(f"Checking at {datetime.datetime.now(datetime.timezone.utc)}")
        for channel in channels:
            print(f'Channel: {channel}')
            async for message in client.iter_messages(channel, offset_date=last_message_time[channel], reverse=True):
                if message.date > last_message_time[channel]:
                    print(f"New message: {message.message}, {message.date}")
                    # Saves latest posts to db
                    last_message_time[channel] = message.date
            print('=====================')
        await asyncio.sleep(15)  

asyncio.run(main())

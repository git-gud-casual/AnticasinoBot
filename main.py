import asyncio
import logging
from datetime import datetime

import config

from telethon import TelegramClient, events
from telethon.tl.types import MessageMediaDice
from telethon.tl.custom.message import Message
from telethon.sessions import StringSession


client = TelegramClient(StringSession(), config.API_ID, config.API_HASH)

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@client.on(events.NewMessage())
async def check_message(event: events.NewMessage.Event):
    msg: Message = event.message
    print(event)
    if isinstance(msg.media, MessageMediaDice) and msg.media.emoticon == '🎰':
        await msg.delete()


async def startup():
    logger.info("Startup bot")
    await client.start(bot_token=config.BOT_TOKEN)
    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(startup())

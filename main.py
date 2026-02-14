#!/usr/bin/env python3

from dotenv import load_dotenv

import os
import simplematrixbotlib as botlib

PREFIX = '!'

load_dotenv()

config = botlib.Config()
config.encryption_enabled = True
config.ignore_unverified_devices = True
creds = botlib.Creds(
    "https://matrix.extratepid.net",
    os.getenv("BOT_USERNAME"),
    os.getenv("BOT_PASSWORD")
)
bot = botlib.Bot(creds, config)


@bot.listener.on_message_event
async def echo(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("echo"):

        await bot.api.send_text_message(
            room.room_id, " ".join(arg for arg in match.args())
            )


bot.run()

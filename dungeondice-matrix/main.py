#!/usr/bin/env python3

from dotenv import load_dotenv
from lib.templates import dicerolls
from lib import dice

import os
import simplematrixbotlib as botlib

PREFIX = '!'

load_dotenv()

config = botlib.Config()
config.encryption_enabled = True
config.ignore_unverified_devices = True
creds = botlib.Creds(
    os.getenv("MATRIX_HOST"),
    os.getenv("BOT_USERNAME"),
    os.getenv("BOT_PASSWORD")
)
bot = botlib.Bot(creds, config)
diceparser = dice.Parser()


@bot.listener.on_message_event
async def echo(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if (
        match.is_not_from_this_bot() and
        match.prefix() and
        (match.command("roll") or match.command("r"))
    ):
        try:
            await bot.api.send_markdown_message(
                room.room_id,
                dicerolls(
                    message.sender,
                    diceparser.parse(match.args()[0]),
                    " ".join(match.args()[1:])
                )
            )
        except Exception as exc:
            print(exc)
            args = " ".join(match.args())
            cmd = f"{PREFIX}{match.command()}"
            await bot.api.send_text_message(
                room.room_id,
                f"Failed on {message.sender}'s command: `{cmd} {args}`"
            )


def start_bot():
    bot.run()

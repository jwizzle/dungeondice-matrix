#!/usr/bin/env python3

import os

import simplematrixbotlib as botlib
from dotenv import load_dotenv

from dungeondice_matrix.lib.commands import (
    PREFIX,
    load_commands,
    matching_command,
)

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


load_commands()


@bot.listener.on_message_event
async def echo(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    command_name = None
    out = False

    if (
        match.is_not_from_this_bot() and
        match.prefix()
    ):
        command_name, handler = matching_command(match)
        if handler:
            try:
                out = handler(match)
                if out:
                    await bot.api.send_markdown_message(
                        room.room_id,
                        out
                    )
            except Exception as exc:
                print(exc)
                args = " ".join(match.args())
                cmd = f"{PREFIX}{command_name}"
                await bot.api.send_text_message(
                    room.room_id,
                    f"Failed on {message.sender}'s command: `{cmd} {args}`"
                )


def start_bot():
    bot.run()

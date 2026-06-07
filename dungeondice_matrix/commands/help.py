#!/usr/bin/env python3

import simplematrixbotlib as botlib

from dungeondice_matrix.lib.commands import PREFIX, available_commands, command
from dungeondice_matrix.lib.templates import commandhelp


@command("help", "h", description="Show available commands.")
def help(match: botlib.MessageMatch):
    return commandhelp(PREFIX, available_commands())

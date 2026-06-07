#!/usr/bin/env python3

import simplematrixbotlib as botlib

from dungeondice_matrix.lib import dice
from dungeondice_matrix.lib.commands import command
from dungeondice_matrix.lib.templates import dicerolls

diceparser = dice.Parser()


@command("roll", "r", description="Roll dice, with an optional comment.")
def roll(match: botlib.MessageMatch):
    return dicerolls(
        match.event.sender,
        diceparser.parse(match.args()[0]),
        " ".join(match.args()[1:])
    )

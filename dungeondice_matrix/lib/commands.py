#!/usr/bin/env python3

from collections.abc import Callable
from dataclasses import dataclass
import importlib
import pkgutil

import simplematrixbotlib as botlib

import dungeondice_matrix.commands

PREFIX = "!"
CommandHandler = Callable[[botlib.MessageMatch], str | bool]


@dataclass
class CommandInfo:
    names: tuple[str, ...]
    description: str
    handler: CommandHandler


COMMANDS: dict[str, CommandInfo] = {}


def command(*names: str, description: str = ""):
    def decorator(func: CommandHandler):
        command_info = CommandInfo(names, description, func)
        for name in names:
            COMMANDS[name] = command_info
        return func

    return decorator


def available_commands():
    seen = set()
    commands = []

    for command_info in COMMANDS.values():
        if id(command_info) not in seen:
            commands.append(command_info)
            seen.add(id(command_info))

    return commands


def load_commands():
    for module in pkgutil.iter_modules(dungeondice_matrix.commands.__path__):
        importlib.import_module(
            f"{dungeondice_matrix.commands.__name__}.{module.name}"
        )


def matching_command(match: botlib.MessageMatch):
    for name, command_info in COMMANDS.items():
        if match.command(name):
            return name, command_info.handler

    return None, None

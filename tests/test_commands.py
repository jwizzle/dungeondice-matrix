from types import SimpleNamespace

import dungeondice_matrix.lib.commands as commands

commands.load_commands()


def test_command_modules_are_loaded_into_registry():
    assert sorted(commands.COMMANDS) == ["c", "calc", "h", "help", "r", "roll"]


def test_available_commands_returns_unique_command_metadata():
    available_commands = commands.available_commands()
    command_names = [command.names for command in available_commands]

    assert ("calc", "c") in command_names
    assert ("help", "h") in command_names
    assert ("roll", "r") in command_names
    assert len(available_commands) == 3


def test_matching_command_returns_alias_and_handler():
    match = SimpleNamespace(command=lambda name: name == "c")

    name, handler = commands.matching_command(match)

    assert name == "c"
    assert handler is commands.COMMANDS["c"].handler


def test_matching_command_returns_none_for_unknown_command():
    match = SimpleNamespace(command=lambda name: False)

    assert commands.matching_command(match) == (None, None)

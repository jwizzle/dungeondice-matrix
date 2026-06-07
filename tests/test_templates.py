from dungeondice_matrix.lib import dice, templates
from dungeondice_matrix.lib.commands import CommandInfo


def noop(_match):
    return False


def test_commandhelp_renders_names_and_descriptions():
    commands = [
        CommandInfo(("roll", "r"), "Roll dice.", noop),
        CommandInfo(("calc", "math"), "Calculate math.", noop),
    ]

    assert templates.commandhelp("!", commands) == """\
**Available commands**

- `!roll`, `!r`: Roll dice.
- `!calc`, `!math`: Calculate math.

"""


def test_calculation_templates():
    assert templates.calculation("2 + 2", 4) == """\
`2 + 2` = **4**
"""
    assert templates.calculation_error("2 +") == """\
Could not calculate `2 +`.
"""


def test_dicerolls_renders_rollgroup_output():
    rollgroup = dice.Rollgroup.from_string("1d6")
    rollgroup.roll(fumble=4)

    assert templates.dicerolls("@user:server", [rollgroup], "damage") == """\
@user:server rolled __damage__
> 1d6
**Total: 4**
_Details: [[4]**+4**]_

"""

import pytest

from dungeondice_matrix.lib import dice


def test_rollstring_accepts_valid_dice_expression():
    assert dice.rollstring("2x2d20(poison)+d8(piercing)-4") == (
        "2x2d20(poison)+d8(piercing)-4"
    )


def test_rollstring_rejects_invalid_dice_expression():
    with pytest.raises(ValueError):
        dice.rollstring("2d6 + code")


def test_rollset_from_string_parses_keep_highest_and_comment():
    rollset = dice.Rollset.from_string("2d20k1(advantage)", negative=False)

    assert rollset.quant == 2
    assert rollset.dice == 20
    assert rollset.keep_amount == 1
    assert rollset.keep_highest is True
    assert rollset.comment == "advantage"


def test_rollgroup_rolls_additions_and_subtractions_with_fumble():
    rollgroup = dice.Rollgroup.from_string("2d6+3-1")

    rollgroup.roll(fumble=4)

    assert rollgroup.total == 10
    assert [rollset.total for rollset in rollgroup.rollsets] == [8, 3, 1]


def test_parser_creates_multiple_rollgroups_for_multipliers_and_commas():
    parser = dice.Parser()

    rollgroups = parser.create_rollgroups("2x1d6,3")

    assert [rollgroup.rollstring for rollgroup in rollgroups] == [
        "1d6",
        "1d6",
        "3",
    ]

import ast
from types import SimpleNamespace

import pytest

from dungeondice_matrix.commands.calc import evaluate, calc


def expression(value: str):
    return ast.parse(value, mode="eval")


def match_with_args(*args: str):
    return SimpleNamespace(args=lambda: list(args))


@pytest.mark.parametrize(
    ("input_value", "expected"),
    [
        ("2 + 3 * 5", 17),
        ("(2 + 3) * 5", 25),
        ("10 / 4", 2.5),
        ("10 // 4", 2),
        ("10 % 4", 2),
        ("2 ** 4", 16),
        ("-(2 + 3)", -5),
    ],
)
def test_evaluate_simple_math(input_value, expected):
    assert evaluate(expression(input_value)) == expected


@pytest.mark.parametrize(
    "input_value",
    [
        "__import__('os').system('date')",
        "sum([1, 2, 3])",
        "[1, 2, 3]",
        "True",
        "2 ** 101",
        "1000000001 + 1",
    ],
)
def test_evaluate_rejects_non_simple_math(input_value):
    with pytest.raises(ValueError):
        evaluate(expression(input_value))


def test_calc_command_renders_result():
    assert calc(match_with_args("2", "+", "3", "*", "5")) == """\
`2 + 3 * 5` = **17**
"""


def test_calc_command_renders_error_for_invalid_expression():
    assert calc(match_with_args("2", "+")) == """\
Could not calculate `2 +`.
"""

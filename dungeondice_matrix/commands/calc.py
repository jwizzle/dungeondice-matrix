#!/usr/bin/env python3

import ast
import operator

import simplematrixbotlib as botlib

from dungeondice_matrix.lib.templates import calculation, calculation_error
from dungeondice_matrix.lib.commands import command

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}
MAX_ABS_VALUE = 1_000_000_000
MAX_POWER = 100


def evaluate(node):
    if isinstance(node, ast.Expression):
        return evaluate(node.body)

    if (
        isinstance(node, ast.Constant) and
        isinstance(node.value, int | float) and
        not isinstance(node.value, bool)
    ):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        left = evaluate(node.left)
        right = evaluate(node.right)

        if type(node.op) is ast.Pow and abs(right) > MAX_POWER:
            raise ValueError("Power is too large.")

        if abs(left) > MAX_ABS_VALUE or abs(right) > MAX_ABS_VALUE:
            raise ValueError("Number is too large.")

        result = OPERATORS[type(node.op)](
            left,
            right
        )
        if abs(result) > MAX_ABS_VALUE:
            raise ValueError("Result is too large.")

        return result

    if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
        result = OPERATORS[type(node.op)](evaluate(node.operand))
        if abs(result) > MAX_ABS_VALUE:
            raise ValueError("Result is too large.")

        return result

    raise ValueError("Not a valid calculation.")


@command("calc", "c", description="Calculate a simple math expression.")
def calc(match: botlib.MessageMatch):
    expression = " ".join(match.args())

    try:
        parsed = ast.parse(expression, mode="eval")
        result = evaluate(parsed)
    except (SyntaxError, ValueError, ZeroDivisionError):
        return calculation_error(expression)

    return calculation(expression, result)

#!/usr/bin/env python3
from dungeondice_matrix.lib import dice


def commandhelp(prefix: str, commands):
    out = ''

    for command in commands:
        names = ", ".join(
            ["`{}{}`".format(prefix, name) for name in command.names]
        )
        out += "- {}: {}\n".format(names, command.description)

    return '''\
**Available commands**

{}
'''.format(out)


def calculation(expression: str, result):
    return '''\
`{}` = **{}**
'''.format(expression, result)


def calculation_error(expression: str):
    return '''\
Could not calculate `{}`.
'''.format(expression)


def dicerolls(author: str, rollgroups: list[dice.Rollgroup], comment: str):
    comment = "__{}__".format(comment) if comment else comment
    out = ''

    for rg in rollgroups:
        out += '''\
> {}
**Total: {}**
_Details: {}_
'''.format(rg.rollstring, rg.total, rg.rollsets)

    return '''\
{} rolled {}
{}
'''.format(author, comment, out)

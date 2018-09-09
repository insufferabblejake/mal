"""
Implements MAL types
"""


class List(list):
    pass


def make_mal_list(*vals):
    return List(vals)


class Symbol(str):
    pass


def make_mal_symbol(token):
    return Symbol(token)

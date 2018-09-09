"""
Implements MAL types
"""

# TODO instead of make_mal_list fns use mal type classes as callables,
# ie. to init


class List(list):
    pass


def make_mal_list(*vals):
    return List(vals)


class Symbol(str):
    pass


def make_mal_symbol(token):
    return Symbol(token)

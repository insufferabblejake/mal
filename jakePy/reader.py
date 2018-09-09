"""
Holds functions that are related to the reader
"""
import re
import malTypes
import exceptions


class BlankLine(Exception):
    pass


class Reader:
    """
    Stateful reader object that stores tokens and a position for a given user
    input line.
    """
    position = None
    token_list = None
    num_tokens = None

    def __init__(self, token_list):
        self.position = 0
        self.token_list = token_list
        self.num_tokens = len(self.token_list)

    def next(self):
        """
        Returns token at current position and increments position
        :return: token at current position
        """
        current_token = self.token_list[self.position]
        self.position += 1
        return current_token

    def peek(self):
        """
        :return: token at current position
        """
        if self.num_tokens > self.position:
            return self.token_list[self.position]
        else:
            return None


def read_str(line=None):
    """
    Will call tokenizer and create a new Reader object instance with the tokens.
    Then calls read_from() with the reader instance.
    :return:
    """
    token_list = tokenizer(line)
    if len(token_list) == 0:
        raise exceptions.BlankLine("Blank line")
    reader = Reader(token_list)
    return read_form(reader)


# TODO Implement the tokenizer without the use of a regex engine
def tokenizer(line=None):
    """
    Takes a string and returns a list of all the tokens in the line.
    :param line: string to be tokenized
    :return: list of tokens
    """
    # compile the regular expression pattern to make future use easier
    pattern = re.compile(
        r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"|;.*|[^\s\[\]{}('"`,;)]*)""")
    # returns a list of tokens(strings), without ''
    return [t for t in re.findall(pattern, line) if t != '']


def read_form(reader=None):
    """
    Stuff
    :param reader: Reader object for a line
    :return: returns a mal data type
    """
    token = reader.peek()
    if token == ')':
        raise Exception("Unexpected ')'")
    elif token == '(':
        return read_list(reader)
    else:
        return read_atom(reader)


def read_list(reader=None):
    """
    Reads a list, aggregates and returns the appropriate ast, which in this
    case is a list.
    :param reader:
    :return: ast -> list
    """
    # in case of a list, the ast we want is a list
    ast = malTypes.make_mal_list()

    token = reader.next()
    if token != '(':
        raise Exception("expected (")

    token = reader.peek()
    while token != ')':
        if not token: raise Exception("expected ) got EOF")
        ast.append(read_form(reader))
        token = reader.peek()

    # Done with processing current list
    # reader.next()
    return ast


def read_atom(reader=None):
    """
    Look at contents of next token in reader and return appropriate
    simple mal type.
    :param reader: reader object
    :return: simple mal type
    """
    token = reader.next()
    integer_pattern = re.compile(r"-?[0-9]+$")
    if re.match(integer_pattern, token):
        return int(token)
    else:
        return malTypes.make_mal_symbol(token)

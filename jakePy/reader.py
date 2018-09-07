"""
Holds functions that are related to the reader
"""
import re


class Reader:
    """
    Stateful reader object that stores tokens and a position.
    """
    current_position = None
    token_list = None
    num_tokens = None

    def __init__(self, token_list):
        self.current_position = 0
        self.token_list = token_list
        self.num_tokens = len(self.token_list)

    def next(self):
        """
        Returns token at current position and increments position
        :return: token at current position
        """
        current_token = self.token_list[self.current_position]
        self.current_position += 1
        return current_token

    def peek(self):
        """
        :return: token at current position
        """
        return self.token_list[self.current_position]


def read_str(line=None):
    """
    Will call tokenizer and create a new Reader object instance with the tokens.
    Then calls read_from() with the reader instance.
    :return:
    """
    reader = Reader(tokenizer(line))
    read_form(reader)


def tokenizer(line=None):
    """
    Takes a string and returns a list of all the tokens in the line.
    :param line: string to be tokenized
    :return: list of tokens
    """
    # compile the regular expression pattern to make future use easier
    pattern = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"|;.*|[^\s\[\]{}('"`,;)]*)""")
    # returns a list of tokens(strings)
    return re.findall(pattern, line)


def read_form(reader=None):
    pass

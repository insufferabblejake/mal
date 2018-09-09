"""
Step 0 of MAL. Creates the skeleton of the interpreter with a pass through eval.
"""
from . import reader


def READ(user_input=None):
    """
    Reads user input
    :param user_input:
    :return:
    """
    read_result = reader.read_str(user_input)
    return read_result


def EVAL(read_result=None):
    """
    Evaluates result of reading user input
    :param read_result:
    :return:
    """
    eval_result = read_result
    return eval_result


def PRINT(eval_result=None):
    """
    Prints result of evaluating user input
    :param eval_result:
    :return:
    """
    print_result = eval_result
    return print_result


def rep(user_input=None):
    """
    The read, eval and print function.
    :param user_input:
    :return:
    """
    return PRINT(EVAL(READ(user_input=user_input)))


# the REPL main loop
while True:
    try:
        print(rep(input("user> ")))
    except EOFError:
        # print a newline before exiting so shell prompt goes to next line
        print("\n")
        break

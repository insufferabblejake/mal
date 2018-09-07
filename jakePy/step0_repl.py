"""
Step 0 of MAL
"""


def READ(user_input=None):
    """
    Reads user input
    :param user_input:
    :return:
    """
    read_result = user_input
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
    Calls READ(), EVAL() and PRINT() passing result of former to latter,
    except READ() which is passed user input.
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

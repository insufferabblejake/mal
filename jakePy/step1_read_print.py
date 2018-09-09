"""
Step 0 of MAL. Creates the skeleton of the interpreter with a pass through eval.
"""
import reader
import printer
import exceptions


def READ(user_input=None):
    """
    Reads user input
    :param user_input:
    :return:
    """
    return reader.read_str(user_input)


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
    return printer.pr_str(eval_result)


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
        line = input("user> ")
        print(rep(line))
    except exceptions.BlankLine:
        continue
    except EOFError:
        # print a newline before exiting so shell prompt goes to next line
        print("\n")
        break

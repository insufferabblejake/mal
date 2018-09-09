"""
Implements the printer
"""
import malTypes


def pr_str(eval_result):
    # TODO instead of isinstance() implement own type checking
    if isinstance(eval_result, malTypes.Symbol):
        return eval_result.__str__()
    elif isinstance(eval_result, int):
        return eval_result.__str__()
    elif isinstance(eval_result, list):
        s = ' '.join([pr_str(val) for val in eval_result])
        return '(' + s + ')'

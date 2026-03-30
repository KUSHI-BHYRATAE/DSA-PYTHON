import operator

def evaluate_prefix(expression):
    stack = []

    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': lambda a, b: a // b,

        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,

        'and': lambda a, b: a and b,
        'or': lambda a, b: a or b,
    }

    tokens = expression.split()[::-1]

    for token in tokens:
        if token.lower() == "true":
            stack.append(True)
        elif token.lower() == "false":
            stack.append(False)
        elif token.lstrip('-').isdigit():
            stack.append(int(token))
        elif token == "not":
            stack.append(not stack.pop())
        elif token in ops:
            a = stack.pop()
            b = stack.pop()
            stack.append(ops[token](a, b))
        else:
            raise ValueError(f"Invalid token: {token}")

    return stack.pop()

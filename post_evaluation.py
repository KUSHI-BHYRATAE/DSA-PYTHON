import operator  # Import built-in module for common operations like +, -, >, etc.

def evaluate_postfix(expression):
    """
    This function evaluates a postfix (Reverse Polish Notation) expression.
    It supports:
    - Arithmetic operators: +, -, *, /
    - Comparison operators: >, <, >=, <=, ==, !=
    - Logical operators: and, or, not
    """

    stack = []  # Create an empty stack (list) to store values during evaluation

    # Dictionary mapping operators (as strings) to actual functions
    ops = {
        # Arithmetic operators
        '+': operator.add,   # addition → a + b
        '-': operator.sub,   # subtraction → a - b
        '*': operator.mul,   # multiplication → a * b
        '/': lambda a, b: a // b,  # integer division → a // b

        # Comparison operators (return True/False)
        '>': operator.gt,    # greater than → a > b
        '<': operator.lt,    # less than → a < b
        '>=': operator.ge,   # greater than or equal → a >= b
        '<=': operator.le,   # less than or equal → a <= b
        '==': operator.eq,   # equal to → a == b
        '!=': operator.ne,   # not equal → a != b

        # Logical operators (return True/False)
        'and': lambda a, b: a and b,
        'or': lambda a, b: a or b,
    }

    # Split the input string into tokens (space-separated)
    # Example: "2 3 *" → ["2", "3", "*"]
    for token in expression.split():

        # -------------------------------
        # CASE 1: Boolean values
        # -------------------------------
        if token.lower() == "true":
            stack.append(True)  # Push True onto stack

        elif token.lower() == "false":
            stack.append(False)  # Push False onto stack

        # -------------------------------
        # CASE 2: Numbers (including negative numbers)
        # -------------------------------
        elif token.lstrip('-').isdigit():
            # lstrip('-') removes minus sign if present
            # isdigit() checks if remaining string is numeric
            stack.append(int(token))  # Convert string → int and push

        # -------------------------------
        # CASE 3: Unary operator (NOT)
        # -------------------------------
        elif token == "not":
            a = stack.pop()        # Pop ONE value from stack
            result = not a         # Apply NOT operation
            stack.append(result)  # Push result back

        # -------------------------------
        # CASE 4: Binary operators
        # -------------------------------
        elif token in ops:
            b = stack.pop()  # Pop top value (second operand)
            a = stack.pop()  # Pop next value (first operand)

            # Apply operation using dictionary
            result = ops[token](a, b)

            stack.append(result)  # Push result back to stack

        # -------------------------------
        # CASE 5: Invalid token
        # -------------------------------
        else:
            raise ValueError(f"Invalid token: {token}")

    # After processing all tokens, only one value should remain
    return stack.pop()

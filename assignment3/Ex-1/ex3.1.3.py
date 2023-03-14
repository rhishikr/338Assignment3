import sys

opr = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b if b != 0 else "Integer divide by zero!"
}

def compute_expression(expression):
    tokens = expression.split()

    stack = []

    for token in reversed(tokens):
        if token.isdigit():
            stack.append(int(token))
        elif token in opr:

            arg1 = stack.pop()
            arg2 = stack.pop()
            if (token == '/' and arg2 == 0):
                return "Integer divide by zero!"
            result = opr[token](arg1, arg2)
            stack.append(result)

    return stack.pop()


def tokenize(expr):
    for i in expr:
        if i not in "1234567890+-/* ":
            expr = expr.replace(i, "")
    return expr


if __name__ == "__main__":
    expression = ""
    for i in sys.argv[1:]:
        expression += i + " "
    expression = tokenize(expression)

    result = compute_expression(expression)
    print(result)
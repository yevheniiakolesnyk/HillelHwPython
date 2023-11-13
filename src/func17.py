def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiplying(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ZeroDivisionError('Division by zero is not allowed')
    else:
        return int(a / b)


def square(a):
    return a ** 2

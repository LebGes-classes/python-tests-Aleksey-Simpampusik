def add(a, b):
    if ((type(a) == int and type(b) == int)
            or (type(a) == float and type(b) == float)
            or (type(a) == int and type(b) == float)
            or (type(a) == float and type(b) == int)):
        return a + b
    else:
        raise TypeError()



def subtract(a, b):
    if ((type(a) == int and type(b) == int)
            or (type(a) == float and type(b) == float)
            or (type(a) == int and type(b) == float)
            or (type(a) == float and type(b) == int)):
        return round(a - b, 1)
    else:
        raise TypeError()


def multiply(a, b):
    if ((type(a) == int and type(b) == int)
            or (type(a) == float and type(b) == float)
            or (type(a) == int and type(b) == float)
            or (type(a) == float and type(b) == int)):
        return a * b
    else:
        raise TypeError()


def divide(a, b):
    if ((type(a) == int and type(b) == int)
            or (type(a) == float and type(b) == float)
            or (type(a) == int and type(b) == float)
            or (type(a) == float and type(b) == int)):
        return a / b
    else:
        raise TypeError()
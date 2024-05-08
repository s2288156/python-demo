x = 100


def p1():
    global x
    x = 102
    print("p1", x)


def p2():
    print("p2", x)


def p3(x1, y):
    """
    :param x1: int
    :param y: int
    :return: int
    """
    return x1 + y


p1()
p2()
result = p3(100, 200)
print(result)

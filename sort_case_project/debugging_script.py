import math


def add(x, y):
    return x + y


a: Literal[3] = 3
b: Literal[4] = 4
c: Literal[7] = add(a,b)
d: float = math.sqrt(b)


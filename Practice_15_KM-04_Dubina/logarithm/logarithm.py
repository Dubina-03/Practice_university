import math

def log(a, b, depth = 0):
    if a**depth == b:
        return depth
    else:
        return log(a, b, depth+1)


def ln(n, depth = 0):
    if math.e**depth == n:
        return depth
    else:
        return ln(n, depth+1)


def lg(n, depth = 0):
    if 10**depth == n:
        return depth
    else:
        return lg(n, depth+1)
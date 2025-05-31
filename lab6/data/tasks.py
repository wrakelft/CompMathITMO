import numpy as np


def f1(x, y):
    return 2 * y + np.exp(x)


def f2(x, y):
    return y / x


def f3(x, y):
    return x ** 2 - y


def f_for_show():
    return "1. 2y + e^x \n 2. y/x \n 3. x^2 - y"


def get_function(f):
    if f == "1":
        return f1
    if f == "2":
        return f2
    if f == "3":
        return f3


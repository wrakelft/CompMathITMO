import numpy as np


def f1(x):
    return 2.74*x**3 - 1.93*x**2 - 15.28*x - 3.72


def f2(x):
    return 2*x**3 + 3.41*x**2 - 23.74*x + 2.95


def f3(x):
    return np.exp(x) - 3*x + 1


def f_for_show():
    return "1. 2.74x^3 - 1.93x^2 - 15.28x - 3.72 \n 2. 2x^3 + 3.41x^2 - 23.74x + 2.95 \n 3. e^x - 3x + 1"


def s_for_show():
    return "1. sin(x + 1) - y - 1.2 \n 2x + cosy - 2 \n 2. x^3 + y^2 - 10 \n x * y + y - 5"


def s11(x, y):
    return np.sin(x + 1) - y - 1.2


def s12(x, y):
    return 2*x + np.cos(y) - 2


def s21(x, y):
    return x**3 + y**2 - 10


def s22(x, y):
    return x * y + y - 5


def get_function(f):
    if f == "1":
        return f1
    if f == "2":
        return f2
    if f == "3":
        return f3


system1 = [s11, s12]
system2 = [s21, s22]


def get_system(f):
    if f == "1":
        return system1
    if f == "2":
        return system2

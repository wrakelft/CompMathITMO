import numpy as np
import functions.linear as linear


def calc_power(xm, ym, p):
    x_log = np.log(xm)
    y_log = np.log(ym)
    a_n, b_n, n, e, s, q, R, r = linear.calc_linear(x_log, y_log, p)
    a = np.exp(b_n)
    b = a_n

    n = a * xm**b
    e = n - ym
    s = np.sum((n - ym) ** 2)
    q = np.sqrt(s / p)
    xfis = np.sum(n) / p
    R = 1 - ((np.sum((ym - n) ** 2)) / (np.sum((ym - xfis) ** 2)))

    return a, b, n, e, s, q, R

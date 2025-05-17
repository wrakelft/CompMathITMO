import numpy as np
import functions.linear as linear


def calc_power(xm, ym):
    x_log = np.log(xm)
    y_log = np.log(ym)
    a_n, b_n = linear.calc_linear(x_log, y_log)
    a = np.exp(a_n)
    b = b_n

    return a, b

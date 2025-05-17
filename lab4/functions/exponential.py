import numpy as np
import functions.linear as linear


def calc_exponential(xm, ym):
    y_log = np.log(ym)
    a_n, b_n = linear.calc_linear(xm, y_log)
    a = np.exp(a_n)
    b = b_n

    return a, b

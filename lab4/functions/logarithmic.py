import numpy as np
import functions.linear as linear


def calc_logarithmic(xm, ym):
    x_log = np.log(xm)
    a_n, b_n = linear.calc_linear(x_log, ym)
    a = a_n
    b = b_n

    return a, b

import numpy as np


def calc(f, x0, y0, xv):
    xv = np.array(xv)
    if f == "1":
        c = (y0 + np.exp(x0)) / np.exp(2 * x0)
        res = c * np.exp(2 * xv) - np.exp(xv)
        return res
    if f == "2":
        c = y0 / x0
        res = c * xv
        return res
    if f == "3":
        c = (y0 + x0 + 1) * np.exp(-x0)
        res = c * np.exp(xv) - xv - 1
        return res

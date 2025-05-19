import numpy as np


def calc_linear(xm, ym, p):
    sx = sum(xm)
    sxx = sum(x**2 for x in xm)
    sy = sum(ym)
    sxy = sum(x * y for x, y in zip(xm, ym))

    d = sxx * p - sx**2
    d1 = sxy * p - sx * sy

    a = d1 / d
    b = (sy - a * sx) / p

    n = a * xm + b
    e = n - ym
    s = np.sum((n - ym) ** 2)
    q = np.sqrt(s / p)
    xfis = np.sum(n) / p
    xsr = np.sum(xm) / p
    ysr = np.sum(ym) / p
    R = 1 - ((np.sum((ym - n)**2)) / (np.sum((ym - xfis)**2)))
    r = (np.sum((xm - xsr) * (ym - ysr))) / (np.sqrt((np.sum((xm - xsr)**2) * np.sum((ym - ysr)**2))))

    return a, b, n, e, s, q, R, r

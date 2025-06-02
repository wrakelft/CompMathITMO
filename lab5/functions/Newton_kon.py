import math


def newton_kon_calc(x, y, table, xim):
    n = len(x)
    h = x[1] - x[0]
    for i in range(1, n - 1):
        if not math.isclose(x[i + 1] - x[i], h, rel_tol=1e-9):
            return 0
    if xim <= (x[0] + x[-1]) / 2:
        t = (xim - x[0]) / h
        res = y[0]
        for i in range(1, n):
            d = table[0][i + 1]
            for j in range(i):
                d *= (t - j) / (j + 1)
            res += d
    else:
        t = (xim - x[-1]) / h
        res = y[-1]
        for i in range(1, n):
            d = table[-i-1][i+1]
            for j in range(i):
                d *= (t + j) / (j + 1)
            res += d

    return res

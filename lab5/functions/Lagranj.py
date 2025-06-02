def lagrange_calc(x, y, xim):
    n = len(x)
    res = 0
    for i in range(n):
        b = 1
        for j in range(n):
            if j == i:
                continue
            b *= (xim - x[j]) / (x[i] - x[j])
        res += y[i] * b
    return res

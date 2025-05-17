def calc_linear(xm, ym):
    n = len(xm)
    sx = sum(xm)
    sxx = sum(x**2 for x in xm)
    sy = sum(ym)
    sxy = sum(x * y for x, y in zip(xm, ym))

    d = sxx * n - (sx**2)
    d1 = sxy * n - sx * sy
    d2 = sxx * sy - sx * sxy

    a = d1 / d
    b = d2 / d

    return a, b


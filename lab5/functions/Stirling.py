import math


def stirling_calc(xs, x, diff_t):
    m = len(xs)
    h = xs[1] - xs[0]
    a = (m - 1) // 2
    x0 = xs[a]
    t = (x - x0) / h
    res = diff_t[a][1]
    prod_even = 1.0
    prod_odd = t
    for k in range(1, m):
        if k % 2 == 1:
            j = (k - 1) // 2
            if j > 0:
                prod_odd *= (t * t - j * j)
            idx = a - j
            if idx > 0:
                d_center = 0.5 * (diff_t[idx][k + 1] + diff_t[idx - 1][k + 1])
            else:
                d_center = diff_t[idx][k + 1]
            term = (prod_odd * d_center) / math.factorial(k)
        else:
            j = k // 2
            if j > 0:
                prod_even *= (t * t - (j - 1) * (j - 1))
            idx = a - j
            term = (prod_even * diff_t[idx][k + 1]) / math.factorial(k)
        res += term
    return res

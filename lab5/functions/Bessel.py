import functions.diff
import math


def bessel_calc(xs, x, diff_t):
    m = len(xs)
    h = xs[1] - xs[0]
    i1 = ((m - 1) // 2) + 1
    i0 = i1 - 1
    x0 = xs[i0]
    t = (x - x0) / h
    diffs = functions.diff.convert_table(diff_t)
    res = 0.5 * (diffs[0][i0] + diffs[0][i1])
    if len(diffs) > 1:
        res += (t - 0.5) * diffs[1][i0]
    max_k = min(len(diffs) - 1, m - 1)
    for k in range(2, max_k + 1):
        if k >= len(diffs):
            break
        if k % 2 == 0:
            j = k // 2
            p = 1.0
            for shift in range(-j, j):
                p *= (t + shift)
            idx = i0 - j + 1
            if 0 <= idx - 1 < len(diffs[k]) and idx < len(diffs[k]):
                diff = 0.5 * (diffs[k][idx] + diffs[k][idx - 1])
                res += p * diff / math.factorial(k)
        else:
            j = (k - 1) // 2
            p = (t - 0.5)
            for shift in range(-j, j):
                p *= (t + shift)
            idx = i0 - j
            if 0 <= idx < len(diffs[k]):
                res += p * diffs[k][idx] / math.factorial(k)
    return res

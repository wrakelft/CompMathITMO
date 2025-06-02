def newton_raz_calc(x, y, xim):
    n = len(x)

    def divided_diff(i, j):
        if j == 0:
            return y[i]
        return (divided_diff(i+1, j-1) - divided_diff(i, j-1)) / (x[i+j] - x[i])

    res = divided_diff(0, 0)
    b = 1

    for i in range(1, n):
        b *= (xim - x[i-1])
        res += divided_diff(0, i) * b

    return res

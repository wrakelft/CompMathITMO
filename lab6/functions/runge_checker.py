def check_runge(less, current, k):
    result = abs(less - current) / (2 ** k - 1)

    return result

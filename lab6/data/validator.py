def validate_interval(x0, xn):
    if x0 >= xn:
        return False
    return True


def validate_eps(eps):
    if eps <= 0 or eps >= 1:
        return False
    return True


def validate_h(h, x0, xn):
    if h <= 0 or h >= (xn - x0):
        return False
    return True



def validate_eps(eps):
    if eps <= 0 or eps > 1:
        return False
    return True


def validate_interval(a, b):
    if a >= b:
        return False
    return True


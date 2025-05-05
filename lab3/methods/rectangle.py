import tasks_enum


def calc_mid(f, a, b, n):
    h = (b - a) / n
    result = 0
    func = tasks_enum.Functions.get_func_lambda(f)
    for i in range(n):
        result += func((a + (i + 0.5) * h))

    return result * h


def calc_left(f, a, b, n):
    h = (b - a) / n
    result = 0
    func = tasks_enum.Functions.get_func_lambda(f)
    for i in range(n):
        result += func((a + i * h))

    return result * h


def calc_right(f, a, b, n):
    h = (b - a) / n
    result = 0
    func = tasks_enum.Functions.get_func_lambda(f)
    for i in range(1, n+1):
        result += func((a + i * h))

    return result * h

import tasks_enum


def calc_trapez(f, a, b, n):
    h = (b - a) / n
    func = tasks_enum.Functions.get_func_lambda(f)
    result = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        result += func(a + i * h)

    return result * h

import tasks_enum


def calc_simpson(f, a, b, n):
    h = (b - a) / n
    func = tasks_enum.Functions.get_func_lambda(f)
    result = func(a) + func(b)
    for i in range(1, n):
        if i % 2 == 1:
            result += 4 * func((a + i * h))
        else:
            result += 2 * func((a + i * h))

    return result * h / 3


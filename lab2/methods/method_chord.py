import additional_functions.validation
import properties.properties
import tasks.task


def calc(e, a, b, f):
    func = tasks.task.get_function(f)
    for n in range(properties.properties.max_iter):
        x_n = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if abs(x_n - b) < e or abs(func(x_n)) < e:
            return x_n, func(x_n), n + 1
        elif additional_functions.validation.has_root(f, x_n, a):
            b = x_n
        else:
            a = x_n
    return 0, 0, 1000

import properties.properties
import properties.properties as pr
import tasks.task


def fabric_df(f):
    h = pr.h

    def df(x):
        return (f(x + h) - f(x - h)) / (2 * h)

    return df


def d_phi(func, lambda_):
    return lambda x: 1 + lambda_ * func(x)


def partial_d(f, x, y, var, sys_num):
    h = properties.properties.h
    system = tasks.task.get_system(f)
    if var == "x":
        f_plus = system[sys_num](x + h, y)
        f_minus = system[sys_num](x - h, y)
        return (f_plus - f_minus) / (2 * h)
    elif var == "y":
        f_plus = system[sys_num](x, y + h)
        f_minus = system[sys_num](x, y - h)
        return (f_plus - f_minus) / (2 * h)



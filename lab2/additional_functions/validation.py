import numpy as np

import additional_functions.derivative
import tasks.task


def validate_interval(a, b):
    if a >= b:
        return False
    return True


def has_root(f, a, b):
    func = tasks.task.get_function(f)
    return func(a) * func(b) < 0


def mono(f, a, b):
    num_points = 100
    func = tasks.task.get_function(f)
    df = additional_functions.derivative.fabric_df(func)
    xes = np.linspace(a, b, num_points)
    der = [df(x) for x in xes]
    all_non_negative = all(d >= 0 for d in der)
    all_non_positive = all(d <= 0 for d in der)
    return all_non_negative or all_non_positive


def has_single_root(f, a, b):
    if not has_root(f, a, b):
        return False

    if not mono(f, a, b):
        return False

    return True


def validate_initial_guess(f, df, x0, eps):
    func = tasks.task.get_function(f)
    if abs(func(x0)) < eps:
        return False

    if df is not None and abs(df(x0)) < eps:
        return False

    return True


def validate_initial_guess_system(system, x0, y0, eps):
    try:
        f1_val = system[0](x0, y0)
        f2_val = system[1](x0, y0)

        if abs(f1_val) < eps and abs(f2_val) < eps:
            return False

        return True
    except Exception as e:
        return False


def validate_eps(eps):
    if eps <= 0 or eps > 1:
        return False
    return True




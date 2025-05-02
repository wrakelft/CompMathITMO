import numpy as np
import additional_functions.derivative
import additional_functions.validation
import properties.properties
import tasks.task


def phi_calc(func, lambda_):
    return lambda x: x + lambda_ * func(x)


def calc(f, a, b, e):
    func = tasks.task.get_function(f)
    df = additional_functions.derivative.fabric_df(func)
    max_df = max(abs(df(a)), abs(df(b)))
    if max_df == 0:
        print('Производная равна нулю на интервале')
        return 0, 0, 0
    if df(a) > 0 and df(b) > 0:
        lambda_ = -1 / max_df
    elif df(a) < 0 and df(b) < 0:
        lambda_ = 1 / max_df
    else:
        print("Не выполняется условие для получения lambda")
        return 0, 0, 0

    phi = phi_calc(func, lambda_)

    dhi = additional_functions.derivative.d_phi(df, lambda_)

    for x in np.linspace(a, b, 10):
        if abs(dhi(x)) >= 1:
            print(f"Условие сходимости нарушено на интервале")
            return 0, 0, 0

    x0 = (a + b) / 2
    for i in range(properties.properties.max_iter):
        x_next = phi(x0)

        if abs(x_next - x0) <= e:
            return x_next, func(x_next), i + 1
        x0 = x_next

    return 0, 0, properties.properties.max_iter

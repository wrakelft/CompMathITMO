import sys
import numpy as np
import data.tasks
import functions.aSolve


def Adams_calc(f, x0, xn, y0, h_init, eps):
    x = [x0]
    y = [y0]
    func = data.tasks.get_function(f)
    for i in range(1, 4):
        if x[-1] >= xn:
            break
        xi = x[-1]
        yi = y[-1]
        h = min(h_init, xn - xi)
        if h < 1e-10:
            break
        k1 = h * func(xi, yi)
        k2 = h * func(xi + h / 2, yi + k1 / 2)
        k3 = h * func(xi + h / 2, yi + k2 / 2)
        k4 = h * func(xi + h, yi + k3)
        yi_pl = yi + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        xi_pl = xi + h
        x.append(xi_pl)
        y.append(yi_pl)
    n = len(y)
    if n < 4:
        print("Нужно минимум 4 точки для Адамса-Бэшфорта 4-го порядка")
        sys.exit(0)
    while x[-1] < xn:
        h = min(h_init, xn - x[-1])
        if h < 1e-10:
            break
        f0 = func(x[-4], y[-4])
        f1 = func(x[-3], y[-3])
        f2 = func(x[-2], y[-2])
        f3 = func(x[-1], y[-1])

        y_pred = y[-1] + h / 24 * (55 * f3 - 59 * f2 + 37 * f1 - 9 * f0)
        x_pred = x[-1] + h

        f_new = func(x_pred, y_pred)
        y_cor = y[-1] + h / 24 * (9 * f_new + 19 * f3 - 5 * f2 + f1)
        x.append(x_pred)
        y.append(y_cor)
    if not np.isclose(x[-1], xn, atol=1e-10):
        x[-1] = xn
    y_exact = [functions.aSolve.calc(f, x0, y0, xin) for xin in x]
    errors = [abs(yin - y_exact_i) for yin, y_exact_i in zip(y, y_exact)]
    max_error = max(errors)
    if max_error > eps:
        print(f"Требуемая точность не достигнута, попробуйте уменьшить шаг! Ошибка = {max_error:.2e} > {eps:.0e}")
    else:
        print(f"Точность достигнута. Ошибка = {max_error:.2e} <= {eps:.0e}")
    return x, y, max_error

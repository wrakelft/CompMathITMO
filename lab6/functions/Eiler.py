import sys

import data.tasks
import functions.runge_checker


def eiler_calc(f, x0, xn, y0, h):
    xv = [x0]
    yv = [y0]
    func = data.tasks.get_function(f)
    while xv[-1] < xn:
        xi = xv[-1]
        yi = yv[-1]
        yi_pl = yi + h * func(xi, yi)
        xi_pl = xi + h
        xv.append(xi_pl)
        yv.append(yi_pl)
    return xv, yv


def eiler_runge_c(f, x0, xn, y0, h_init, eps, k=1):
    h = h_init
    while True:
        xh, yh = eiler_calc(f, x0, xn, y0, h)
        yn_h = yh[-1]
        xh2, yh2 = eiler_calc(f, x0, xn, y0, h / 2)
        yn_h2 = yh2[-1]
        error = functions.runge_checker.check_runge(yn_h, yn_h2, k)
        if error <= eps:
            break
        h = h / 2
        if h < 1e-10:
            print("Точность не достигнута")
            sys.exit(0)
    return xh, yh, h, error

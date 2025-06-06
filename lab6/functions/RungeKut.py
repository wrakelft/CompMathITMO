import sys
import data.tasks
import functions.runge_checker


def runge_calc(f, x0, xn, y0, h):
    xv = [x0]
    yv = [y0]
    func = data.tasks.get_function(f)
    while xv[-1] < xn:
        xi = xv[-1]
        yi = yv[-1]
        if xi + h > xn:
            break
        k1 = h * func(xi, yi)
        k2 = h * func(xi + h / 2, yi + k1 / 2)
        k3 = h * func(xi + h / 2, yi + k2 / 2)
        k4 = h * func(xi + h, yi + k3)
        yi_pl = yi + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        xi_pl = xi + h
        xv.append(xi_pl)
        yv.append(yi_pl)
    return xv, yv


def runge_with_c(f, x0, xn, y0, h_init, eps, k=4):
    h = h_init
    while True:
        xh, yh = runge_calc(f, x0, xn, y0, h)
        yn_h = yh[-1]
        xh2, yh2 = runge_calc(f, x0, xn, y0, h / 2)
        yn_h2 = yh2[-1]
        error = functions.runge_checker.check_runge(yn_h, yn_h2, k)
        if error <= eps:
            break
        h = h / 2
        if h < 1e-10:
            print("Точность не достигнута")
            sys.exit(0)
    return xh, yh, h, error

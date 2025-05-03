import additional_functions.derivative
import numpy as np

import properties.properties
import tasks.task


def build_jac(f, x, y):
    df1_dx = additional_functions.derivative.partial_d(f, x, y, 'x', 0)
    df1_dy = additional_functions.derivative.partial_d(f, x, y, 'y', 0)
    df2_dx = additional_functions.derivative.partial_d(f, x, y, 'x', 1)
    df2_dy = additional_functions.derivative.partial_d(f, x, y, 'y', 1)

    J = np.array([[df1_dx, df1_dy], [df2_dx, df2_dy]])

    return J


def newton_system_calc(f, x, y, e):
    x0, y0 = x, y
    system = tasks.task.get_system(f)
    print("№ |     x0   |     y0    |    x_n   |    y_n    | |x_n - x0| | |y_n - y0|")
    for i in range(properties.properties.max_iter):
        f1_val = system[0](x0, y0)
        f2_val = system[1](x0, y0)

        J = build_jac(f, x0, y0)

        if np.abs(np.linalg.det(J)) < 1e-12:
            print("Матрица близка к 0!")
            return 0, 0, 0, 0, 0

        rhs = -np.array([f1_val, f2_val])
        dx, dy = np.linalg.solve(J, rhs)

        x_n = x0 + dx
        y_n = y0 + dy

        print(
            f"{i + 1} | {x0:.6f} | {y0:.6f} | {x_n:.6f} | {y_n:.6f} | {abs(x_n - x0):.6f} | {abs(y_n - y0):.6f}")

        if abs(x_n - x0) <= e and abs(y_n - y0) <= e:
            return x_n, y_n, i + 1, abs(x_n - x0), abs(y_n - y0)

        x0 = x_n
        y0 = y_n

    print("Метод не сошелся за максимальное кол-во итераций")
    return 0, 0, properties.properties.max_iter, 0, 0



import numpy as np
import matplotlib.pyplot as plt

import tasks.task


def plot_single_f(func, a, b):
    x = np.linspace(a, b, 500)
    y = func(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=func.__name__)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_system(system):
    x_range = (-15, 15)
    y_range = (-15, 15)

    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(x_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x, y)

    plt.figure(figsize=(10, 8))

    plt.contour(X, Y, system[0](X, Y), levels=[0], colors='r')
    plt.contour(X, Y, system[1](X, Y), levels=[0], colors='b')

    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Система уравнений\nКрасная: {format_eq(system[0])} = 0\nСиняя: {format_eq(system[1])} = 0')
    plt.show()


def plot_selector(f_type, f, a=None, b=None):
    if f_type == 'single':
        func = tasks.task.get_function(f)
        plot_single_f(func, a, b)
    elif f_type == 'system':
        if f == '1':
            plot_system(tasks.task.system1)
        elif f == '2':
            plot_system(tasks.task.system2)


def format_eq(func):
    name = func.__name__
    name = name.replace('s11', 'sin(x + 1) - y - 1.2')
    name = name.replace('s12', '2x + cosy - 2')
    name = name.replace('s21', 'sin(x + y) - 1.1x - 0.1')
    name = name.replace('s22', 'x^2 + y^2 - 1')
    return name


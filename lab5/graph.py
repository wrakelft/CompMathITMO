import numpy as np
import matplotlib.pyplot as plt
import functions.Newton_kon
import functions.Newton_raz
import functions.Lagranj
import functions.Stirling
import functions.Bessel
from tqdm import tqdm


def plot_all_methods(x, y, diff_table, xim, flag, nk_flag):
    x_plot = np.linspace(min(x), max(x), 100)

    tqdm.write("Вычисление интерполяции Лагранжа...")
    y_lagrange = []
    for xi in tqdm(x_plot):
        y_lagrange.append(functions.Lagranj.lagrange_calc(x, y, xi))

    tqdm.write("Вычисление интерполяции Ньютона (раздел. разности)...")
    y_newton_raz = []
    for xi in tqdm(x_plot):
        y_newton_raz.append(functions.Newton_raz.newton_raz_calc(x, y, xi))

    if nk_flag == 0:
        tqdm.write("Вычисление интерполяции Ньютона (конеч. разности)...")
        y_newton_kon = []
        for xi in tqdm(x_plot):
            y_newton_kon.append(functions.Newton_kon.newton_kon_calc(x, y, diff_table, xi))

    if flag == 1:
        tqdm.write("Вычисление интерполяции Стерлинга...")
        y_spec = []
        for xi in tqdm(x_plot):
            y_spec.append(functions.Stirling.stirling_calc(x, xi, diff_table))
        special_label = 'Стирлинг'
        special_color = 'm-.'
        y_test_spec = functions.Stirling.stirling_calc(x, xim, diff_table)
    else:
        tqdm.write("Вычисление интерполяции Бесселя...")
        y_spec = []
        for xi in tqdm(x_plot):
            y_spec.append(functions.Bessel.bessel_calc(x, xi, diff_table))
        special_label = 'Бессель'
        special_color = 'c-'
        y_test_spec = functions.Bessel.bessel_calc(x, xim, diff_table)

    plt.figure(figsize=(12, 7))

    plt.scatter(x, y, color='black', s=100,
                label='Узлы интерполяции', zorder=5)

    plt.plot(x_plot, y_lagrange, 'r-', linewidth=2, label='Лагранж')
    plt.plot(x_plot, y_newton_raz, 'g--', linewidth=2, label='Ньютон (раздел. разности)')

    if nk_flag == 0:
        plt.plot(x_plot, y_newton_kon, 'b:', linewidth=2, label='Ньютон (конеч. разности)')

    plt.plot(x_plot, y_spec, special_color, linewidth=2, label=special_label)

    y_test_lag = functions.Lagranj.lagrange_calc(x, y, xim)
    y_test_nr = functions.Newton_raz.newton_raz_calc(x, y, xim)
    # y_test_nk = functions.Newton_kon.newton_kon_calc(x, y, diff_table, xim)

    if nk_flag != 1:
        y_test_nk = functions.Newton_kon.newton_kon_calc(x, y, diff_table, xim)
        plt.scatter([xim] * 4, [y_test_lag, y_test_nr, y_test_nk, y_test_spec],
                    color=['red', 'green', 'blue', special_color[0]], s=80, zorder=6)
    else:
        plt.scatter([xim] * 3, [y_test_lag, y_test_nr, y_test_spec],
                    color=['red', 'green', special_color[0]], s=80, zorder=6)

    plt.axvline(x=xim, color='gray', linestyle='--', alpha=0.5)

    # Настройки отображения
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.title('Сравнение методов интерполяции', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)

    plt.tight_layout()
    plt.show()

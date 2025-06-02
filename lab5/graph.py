import numpy as np
import matplotlib.pyplot as plt
import functions.Newton_kon
import functions.Newton_raz
import functions.Lagranj
from tqdm import tqdm


def plot_all_methods(x, y, diff_table, xim):
    x_plot = np.linspace(min(x), max(x), 100)

    # Добавляем прогресс-бар
    tqdm.write("Вычисление интерполяции Лагранжа...")
    y_lagrange = []
    for xi in tqdm(x_plot):
        y_lagrange.append(functions.Lagranj.lagrange_calc(x, y, xi))

    tqdm.write("Вычисление интерполяции Ньютона (раздел. разности)...")
    y_newton_raz = []
    for xi in tqdm(x_plot):
        y_newton_raz.append(functions.Newton_raz.newton_raz_calc(x, y, xi))

    tqdm.write("Вычисление интерполяции Ньютона (конеч. разности)...")
    y_newton_kon = []
    for xi in tqdm(x_plot):
        y_newton_kon.append(functions.Newton_kon.newton_kon_calc(x, y, diff_table, xi))

    # y_lagrange = [functions.Lagranj.lagrange_calc(x, y, xi) for xi in x_plot]
    # y_newton_raz = [functions.Newton_raz.newton_raz_calc(x, y, xi) for xi in x_plot]
    # y_newton_kon = [functions.Newton_kon.newton_kon_calc(x, y, diff_table, xi) for xi in x_plot]

    plt.figure(figsize=(12, 7))

    plt.scatter(x, y, color='black', s=100,
                label='Узлы интерполяции', zorder=5)

    plt.plot(x_plot, y_lagrange, 'r-', linewidth=2, label='Лагранж')
    plt.plot(x_plot, y_newton_raz, 'g--', linewidth=2, label='Ньютон (раздел. разности)')
    plt.plot(x_plot, y_newton_kon, 'b:', linewidth=2, label='Ньютон (конеч. разности)')

    y_test_lag = functions.Lagranj.lagrange_calc(x, y, xim)
    y_test_nr = functions.Newton_raz.newton_raz_calc(x, y, xim)
    y_test_nk = functions.Newton_kon.newton_kon_calc(x, y, diff_table, xim)

    plt.scatter([xim] * 3, [y_test_lag, y_test_nr, y_test_nk],
                color=['red', 'green', 'blue'], s=80, zorder=6)
    plt.axvline(x=xim, color='gray', linestyle='--', alpha=0.5)

    # Настройки отображения
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.title('Сравнение методов интерполяции', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)

    # plt.text(xim + 0.02, y_test_lag, f'L({xim:.2f})={y_test_lag:.4f}', color='red', va='center')
    # plt.text(xim + 0.02, y_test_nr, f'Nd({xim:.2f})={y_test_nr:.4f}', color='green', va='center')
    # plt.text(xim + 0.02, y_test_nk, f'Nf({xim:.2f})={y_test_nk:.4f}', color='blue', va='center')

    plt.tight_layout()
    plt.show()

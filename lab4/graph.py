import matplotlib.pyplot as plt
import numpy as np


def plot_all_functions(x, y, models_results):
    plt.figure(figsize=(12, 8))

    plt.scatter(x, y, color='black', s=50, label='Исходные данные', zorder=5)

    x_smooth = np.linspace(min(x) - 1, max(x) + 1, 500)

    for name, data in models_results.items():
        coeffs = data['coeffs']

        if name == 'Линейная':
            y_smooth = coeffs[0] * x_smooth + coeffs[1]
        elif name == 'Полином2СТ':
            y_smooth = coeffs[0] * x_smooth**2 + coeffs[1] * x_smooth + coeffs[2]
        elif name == 'Полином3СТ':
            y_smooth = coeffs[0] * x_smooth**3 + coeffs[1] * x_smooth**2 + coeffs[2] * x_smooth + coeffs[3]
        elif name == 'Экспоненциальная':
            y_smooth = coeffs[0] * np.exp(coeffs[1] * x_smooth)
        elif name == 'Логарифмическая':
            y_smooth = coeffs[0] * np.log(x_smooth) + coeffs[1]
        elif name == 'Степенная':
            y_smooth = coeffs[0] * x_smooth**coeffs[1]

        plt.plot(x_smooth, y_smooth,
                 label=f"{name}")

    plt.title("Сравнение аппроксимирующих функций", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=10)

    plt.show()
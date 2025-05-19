import numpy as np
from tabulate import tabulate


def print_model_results(model_name, x, y, fi, a, b, c, d, S, eps, mse, r2, pearson=None):
    print("\n" + "=" * 50)
    print(f"МОДЕЛЬ: {model_name.upper()}")
    print("=" * 50)

    print("\nТаблица значений:")
    print(tabulate({
        "x": x,
        "y": y,
        f"φ(x) ({model_name})": fi,
        "ε": eps
    }, headers="keys", floatfmt=".4f", showindex=False))

    print("\nКоэффициенты:")
    if model_name == 'Линейная' or model_name == 'Экспоненциальная' or model_name == 'Логарифмическая' or model_name == 'Степенная':
        print(f"a = {a:.6f}, b = {b:.6f}")
    elif model_name == 'Полином 2-ст':
        print(f"a = {a:.6f}, b = {b:.6f}, c = {c:.6f}")
    elif model_name == 'Полином 3-ст':
        print(f"a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, d = {d:.6f}")

    print(f"\nМера отклонения (S): {S:.6f}")
    print(f"Среднеквадратичное отклонение (СКО): {mse:.6f}")
    print(f"Коэффициент детерминации (R²): {r2:.6f}")

    if pearson is not None:
        print(f"Коэффициент корреляции Пирсона: {pearson:.6f}")

    print("\nИнтерпретация R²:")
    if r2 >= 0.95:
        print("Высокое соответствие модели данным (R² ≥ 0.95)")
    elif r2 >= 0.75:
        print("Удовлетворительное соответствие модели данным (0.75 ≤ R² < 0.95)")
    elif r2 >= 0.5:
        print("Слабое соответствие модели данным (0.5 ≤ R² < 0.75)")
    else:
        print("Недостаточное соответствие модели данным (R² < 0.5)")


def print_best_model(q_l, q_p2, q_p3, q_e, q_log, q_st):
    best = min(q_l, q_p2, q_p3, q_e, q_log, q_st)
    name = ""
    if q_l == best:
        name = "Линейная"
    elif q_p2 == best:
        name = "Полином 2-ст"
    elif q_p3 == best:
        name = "Полином 3-ст"
    elif q_e == best:
        name = "Экспоненциальная"
    elif q_log == best:
        name = "Логарифмическая"
    elif q_st == best:
        name = "Степенная"

    print("\n" + "=" * 50)
    print("ИТОГОВЫЙ РЕЗУЛЬТАТ")
    print("=" * 50)
    print(f"Наилучшая модель: {name.upper()}")
    print(f"Среднеквадратичное отклонение (СКО): {best:.6f}")


def form_output_main(model_name, x, y, fi, a, b, c, d, S, eps, mse, r2, s, pearson=None):
    s += "\n" + "=" * 50
    s += f"МОДЕЛЬ: {model_name.upper()}"
    s += ("=" * 50)

    s += "\nТаблица значений:\n"
    s += (tabulate({
        "x": x,
        "y": y,
        f"φ(x) ({model_name})": fi,
        "ε": eps
    }, headers="keys", floatfmt=".4f", showindex=False))

    s += "\nКоэффициенты:\n"
    if model_name == 'Линейная' or model_name == 'Экспоненциальная' or model_name == 'Логарифмическая' or model_name == 'Степенная':
        s += f"a = {a:.6f}, b = {b:.6f}\n"
    elif model_name == 'Полином 2-ст':
        s += f"a = {a:.6f}, b = {b:.6f}, c = {c:.6f}\n"
    elif model_name == 'Полином 3-ст':
        s += f"a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, d = {d:.6f}\n"

    s += f"\nМера отклонения (S): {S:.6f}\n"
    s += f"Среднеквадратичное отклонение (СКО): {mse:.6f}\n"
    s += f"Коэффициент детерминации (R²): {r2:.6f}\n"

    if pearson is not None:
        s += f"Коэффициент корреляции Пирсона: {pearson:.6f}\n"

    s += "\nИнтерпретация R²:\n"
    if r2 >= 0.95:
        s += "Высокое соответствие модели данным (R² ≥ 0.95)\n"
    elif r2 >= 0.75:
        s += "Удовлетворительное соответствие модели данным (0.75 ≤ R² < 0.95)\n"
    elif r2 >= 0.5:
        s += "Слабое соответствие модели данным (0.5 ≤ R² < 0.75)\n"
    else:
        s += "Недостаточное соответствие модели данным (R² < 0.5)\n"

    return s


def form_best_model(q_l, q_p2, q_p3, q_e, q_log, q_st, s):
    best = min(q_l, q_p2, q_p3, q_e, q_log, q_st)
    name = ""
    if q_l == best:
        name = "Линейная"
    elif q_p2 == best:
        name = "Полином 2-ст"
    elif q_p3 == best:
        name = "Полином 3-ст"
    elif q_e == best:
        name = "Экспоненциальная"
    elif q_log == best:
        name = "Логарифмическая"
    elif q_st == best:
        name = "Степенная"

    s += "\n" + "=" * 50 + "\n"
    s += "ИТОГОВЫЙ РЕЗУЛЬТАТ\n"
    s += "=" * 50 + "\n"
    s += f"Наилучшая модель: {name.upper()}\n"
    s += f"Среднеквадратичное отклонение (СКО): {best:.6f}\n"

    return s


def save_file(string):
    with open("out.txt", "w", encoding="utf-8") as file:
        file.write(string)
        print("Файл заполнен!")

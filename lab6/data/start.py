import data.tasks
import data.inpt
import sys
import functions.Eiler
import functions.aSolve
import functions.drow


def user_inout():
    try:
        f = ""
        while f != "1" and f != "2" and f != "3":
            f = input("Выберите уравнение: \n " + data.tasks.f_for_show() + "\n")
        if f == "1" or f == "2" or f == "3":
            m = ""
            while m != "1" and m != "2" and m != "3":
                m = input("Выберите метод решения: \n 1. Эйлера \n 2. Рунге-Кутта 4-го порядка \n 3. Адамс \n")
            x0, xn, y0, h, e = data.inpt.from_keyboard(f)
            if m == "1":
                x, y, h, error = functions.Eiler.eiler_runge_c(f, x0, xn, y0, h, e)
                y_res = functions.aSolve.calc(f, x0, y0, x)
                print_res(x, y, y_res, h, error)
                functions.drow.plot_solutions(x, y, y_res)
    except EOFError:
        print("Завершаем выполнение программы.")
        sys.exit(0)


def print_res(x, y, res, h, error):
    print("\nРезультаты численного решения:")
    print("-" * 40)
    print("|     x     |     y(x)     |     y точное     |")
    print("-" * 40)
    for xv, yv, yt in zip(x, y, res):
        print(f"| {xv:9.5f} | {yv:12.6f} | {yt:9.6f}")
    print("-" * 40)
    print(f"\nФинальный шаг: {h}")
    print(f"\nОшибка на концах интервала по правилу Рунге: {error}")

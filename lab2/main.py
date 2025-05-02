# Метод хорд
# Метод Ньютона
# Метод простой итерации
# Метод Ньютона (Система)
import additional_functions.validation
import additional_functions.derivative
import additional_functions.drow_graph
import methods.method_chord
import methods.simple_iter_method
import methods.newton_method
import tasks.task
import sys


def from_keyboard(f, m, i):
    while True:
        try:
            e = float(input("Введите точность системы >0 и <1: ").replace(',', '.'))
            if not additional_functions.validation.validate_eps(e):
                print("Точность не может быть меньше 0 или больше 1")
                sys.exit(1)
            if m == "1" or m == "3":
                a, b = map(float, input("Введите интервал через пробел: ").replace(',', '.').split())
                if not additional_functions.validation.validate_interval(a, b):
                    print("Левая граница не может быть меньше или равна правой!")
                    sys.exit(1)
                elif not additional_functions.validation.has_single_root(f, a, b):
                    print("На интервале нет корней или больше 1 корня!")
                    sys.exit(1)
                return e, a, b
            elif m == "2" and i == "s":
                x0, y0 = map(float, input("Введите x0 и y0 для системы через пробел: ").replace(',', '.').split())
                if not additional_functions.validation.validate_initial_guess_system(tasks.task.get_system(f), x0, y0, e):
                    print("Начальное приближение некорректно, вы попали в корень")
                    sys.exit(1)
                return e, x0, y0
            elif m == "2":
                x0 = float(input("Введите начальное приближение: ").replace(',', '.'))
                if not additional_functions.validation.validate_initial_guess(f, None, x0, e):
                    print("Начальное приближение некорректно, вы попали в корень")
                    sys.exit(1)
                return e, x0
        except ValueError:
            print("Вводите числа! Для интервала и приближения для системы - два через пробел, для начального приближения только одно!")
        except EOFError:
            print("Завершаем выполнение программы.")
            sys.exit(0)


def from_file(filename, f, m, i):
    try:
        with open(filename, "r", encoding="utf-8") as fi:
            lines = [line.strip() for line in fi if line.strip()]
            if len(lines) != 2:
                print("Неверная структура данных в файле!")
                sys.exit(1)
        e = float(lines[0].replace(',', '.'))
        if not additional_functions.validation.validate_eps(e):
            print("Точность не может быть меньше 0 или больше 1")
            sys.exit(1)
        if m == "1" or m == "3":
            a, b = map(float, lines[1].replace(',', '.').split())
            if not additional_functions.validation.validate_interval(a, b):
                print("Левая граница не может быть меньше или равна правой!")
                sys.exit(1)
            elif not additional_functions.validation.has_single_root(f, a, b):
                print("На интервале нет корней или больше 1 корня!")
                sys.exit(1)
            return e, a, b
        elif m == "2" and i == "s":
            x0, y0 = map(float, lines[1].replace(',', '.').split())
            if not additional_functions.validation.validate_initial_guess_system(tasks.task.get_system(f), x0, y0, e):
                print("Начальное приближение некорректно, вы попали в корень")
                sys.exit(1)
            return e, x0, y0
        elif m == "2":
            x0 = float(lines[1].replace(',', '.'))
            if not additional_functions.validation.validate_initial_guess(f, None, x0, e):
                print("Начальное приближение некорректно, вы попали в корень")
                sys.exit(1)
            return e, x0
    except ValueError:
        print("Вводите числа! Для интервала и приближения для системы - два через пробел, для начального приближения только одно!")
        sys.exit(1)
    except FileNotFoundError:
        print("Файл не найден")
        sys.exit(1)
    except PermissionError:
        print("Нет прав для доступа к файлу")
        sys.exit(1)
    except IsADirectoryError:
        print("Указана директория вместо файла")
        sys.exit(1)
    except UnicodeDecodeError:
        print("Проблема с кодировкой файла")
        sys.exit(1)


def start():
    try:
        i = ""
        while i != "y" and i != "s":
            i = input("Выберите объект решения: уравнение - y или систему уравнений - s: ")
        if i == "y":
            f = ""
            while f != "1" and f != "2" and f != "3":
                f = input("Выберите уравнение: \n " + tasks.task.f_for_show() + "\n")
            if f == "1" or f == "2" or f == "3":
                m = ""
                while m != "1" and m != "2" and m != "3":
                    m = input("Выберите метод решения: \n 1. Метод хорд \n 2. Метод Ньютона \n 3. Метод простых итераций \n")
                if m == "1" or m == "2" or m == "3":
                    inp = ""
                    while inp != "f" and inp != "k":
                        inp = input("Выберите откуда ввести границы интервала/начальное приближение и погрешность. f - из файла, k - с клавиатуры: ")
                    outer = ""
                    while outer != "f" and outer != "m":
                        outer = input("Выберите куда вывести результаты. f - в файл, m - на экран: ")
                    if inp == "k":
                        if m == "1":
                            e, a, b = from_keyboard(f, m, i)
                            x_n, function, iter_count = methods.method_chord.calc(e, a, b, f)
                            if outer == "m":
                                print(f"x: {x_n:.6f}")
                                print(f"f(x): {function}")
                                print(f"Кол-во итераций: {iter_count}")
                            if outer == "f":
                                with open("out.txt", "w") as file:
                                    file.write("МЕТОД ХОРД\n")
                                    file.write(f"Корень методом Хорд: {x_n:.6f}\n")
                                    file.write(f"Значение функции в корне: {function}\n")
                                    file.write(f"Кол-во итераций: {iter_count}\n")
                                    print("Файл заполнен!")
                            print("Закройте окно с показом функции чтобы завершить программу")
                            additional_functions.drow_graph.plot_selector("single", f, a, b)
                        elif m == "2":
                            e, x0 = from_keyboard(f, m, i)
                            x_n, function, iter_count = methods.newton_method.calc_newton(f, x0, e)
                            if outer == "m":
                                print(f"x: {x_n:.6f}")
                                print(f"f(x): {function}")
                                print(f"Кол-во итераций: {iter_count}")
                            if outer == "f":
                                with open("out.txt", "w") as file:
                                    file.write("МЕТОД НЬЮТОНА\n")
                                    file.write(f"Корень методом Ньютона: {x_n:.6f}\n")
                                    file.write(f"Значение функции в корне: {function}\n")
                                    file.write(f"Кол-во итераций: {iter_count}\n")
                                    print("Файл заполнен!")
                            print("Закройте окно с показом функции чтобы завершить программу")
                            additional_functions.drow_graph.plot_selector("single", f, -5, 5)
                        elif m == "3":
                            e, a, b = from_keyboard(f, m, i)
                            x_n, function, iter_count = methods.simple_iter_method.calc(f, a, b, e)
                            if outer == "m":
                                print(f"x: {x_n:.6f}")
                                print(f"f(x): {function}")
                                print(f"Кол-во итераций: {iter_count}")
                            if outer == "f":
                                with open("out.txt", "w") as file:
                                    file.write("МЕТОД ПРОСТОЙ ИТЕРАЦИИ\n")
                                    file.write(f"Корень методом простой итерации: {x_n:.6f}\n")
                                    file.write(f"Значение функции в корне: {function}\n")
                                    file.write(f"Кол-во итераций: {iter_count}\n")
                                    print("Файл заполнен!")
                            print("Закройте окно с показом функции чтобы завершить программу")
                            additional_functions.drow_graph.plot_selector("single", f, a, b)
                    elif inp == "f":
                        print("Первая строка файла всегда должна быть значением точности >0 и <1")
                        print("Вторая строка файла должна быть интервалом для метода хорд и простых итераций (два числа через пробел) или начальным приближением для всех остальных методов(одно число для уравнения и два для системы)")
                        filename = input("Введите имя файла: ").strip()
                        if m == "1":
                            e, a, b = from_file(filename, f, m, i)
                            x_n, function, iter_count = methods.method_chord.calc(e, a, b, f)
                            if outer == "m":
                                print(f"Корень методом Хорд: {x_n:.6f}")
                                print(f"Значение функции в корне: {function}")
                                print(f"Кол-во итераций: {iter_count}")
                            elif outer == "f":
                                with open("out.txt", "w") as file:
                                    file.write("МЕТОД ХОРД\n")
                                    file.write(f"Корень методом Хорд: {x_n:.6f}\n")
                                    file.write(f"Значение функции в корне: {function}\n")
                                    file.write(f"Кол-во итераций: {iter_count}\n")
                                    print("Файл заполнен!")
                            print("Закройте окно с показом функции чтобы завершить программу")
                            additional_functions.drow_graph.plot_selector("single", f, a, b)
                        elif m == "2":
                            e, x0 = from_file(filename, f, m, i)
                            x_n, function, iter_count = methods.newton_method.calc_newton(f, x0, e)
                            if outer == "m":
                                print(f"x: {x_n:.6f}")
                                print(f"f(x): {function}")
                                print(f"Кол-во итераций: {iter_count}")
                            if outer == "f":
                                with open("out.txt", "w") as file:
                                    file.write("МЕТОД НЬЮТОНА\n")
                                    file.write(f"Корень методом Ньютона: {x_n:.6f}\n")
                                    file.write(f"Значение функции в корне: {function}\n")
                                    file.write(f"Кол-во итераций: {iter_count}\n")
                                    print("Файл заполнен!")
                            print("Закройте окно с показом функции чтобы завершить программу")
                            additional_functions.drow_graph.plot_selector("single", f, -5, 5)
                        elif m == "3":
                            e, a, b = from_file(filename, f, m, i)
                            x_n, function, iter_count = methods.simple_iter_method.calc(f, a, b, e)
                            if outer == "m":
                                print(f"x: {x_n:.6f}")
                                print(f"f(x): {function}")
                                print(f"Кол-во итераций: {iter_count}")
                            if outer == "f":
                                with open("out.txt", "w") as file:
                                    file.write("МЕТОД ПРОСТОЙ ИТЕРАЦИИ\n")
                                    file.write(f"Корень методом простой итерации: {x_n:.6f}\n")
                                    file.write(f"Значение функции в корне: {function}\n")
                                    file.write(f"Кол-во итераций: {iter_count}\n")
                                    print("Файл заполнен!")
                            print("Закройте окно с показом функции чтобы завершить программу")
                            additional_functions.drow_graph.plot_selector("single", f, a, b)
        elif i == "s":
            f = ""
            while f != "1" and f != "2":
                f = input("Выберите систему: \n " + tasks.task.s_for_show() + "\n")
            if f == "1" or f == "2":
                    inp = ""
                    while inp != "f" and inp != "k":
                        inp = input(
                            "Выберите откуда ввести начальное приближение и погрешность. f - из файла, k - с клавиатуры: ")
                    outer = ""
                    while outer != "f" and outer != "m":
                        outer = input("Выберите куда вывести результаты. f - в файл, m - на экран: ")
                    if inp == "k":
                        e, x0, y0 = from_keyboard(f, "2", i)
                        additional_functions.drow_graph.plot_selector("system", f, -5, 5)
                    elif inp == "f":
                        print("Первая строка файла всегда должна быть значением точности >0 и <1")
                        print("Вторая строка файла должна быть интервалом для метода хорд и простых итераций (два числа через пробел) или начальным приближением для всех остальных методов(одно число для уравнения и два для системы)")
                        filename = input("Введите имя файла: ").strip()
                        e, x0, y0 = from_file(filename, f, "2", i)
                        additional_functions.drow_graph.plot_selector("system", f, -5, 5)
                        # продолжение решения
    except EOFError:
        print("Завершаем выполнение программы.")
        sys.exit(0)



if __name__ == '__main__':
    start()



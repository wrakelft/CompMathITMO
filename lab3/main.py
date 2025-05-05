import sys
import tasks_enum
import validation.input_validator
import validation.runge_checker
import methods.rectangle
import methods.trapez
import methods.simpson


def inp():
    while True:
        try:
            e = float(input("Введите точность системы >0 и <1: ").replace(',', '.'))
            if not validation.input_validator.validate_eps(e):
                print("Точность не может быть меньше 0 или больше 1")
                raise ValueError
            a, b = map(float, input("Введите интервал через пробел: ").replace(',', '.').split())
            if not validation.input_validator.validate_interval(a, b):
                print("Левая граница не может быть меньше или равна правой!")
                raise ValueError
            return e, a, b
        except ValueError:
            print("Вводите числа! Для интервала два через пробел (первое < второе), для точности только одно!")
        except EOFError:
            print("Завершаем выполнение программы.")
            sys.exit(0)


def start():
    try:
        f = ""
        while f != "one" and f != "two" and f != "three" and f != "four":
            f = input("Выберите функцию из списка:\n " + tasks_enum.Functions.show_all_func() + "Введите one, two, three или four для выбора: ")
        if f == "one" or f == "two" or f == "three" or f == "four":
            m = ""
            while m != "1" and m != "2" and m != "3" and m != "4" and m != "5":
                m = input("Выберите метод решения: \n 1. Левые прям. \n 2. Средние прям. \n 3. Правые прям. \n 4. Трапеции \n 5. Симпсона \n")
            print("Начальное значение разбиения интервала: 4")
            n = 4
            e, a, b = inp()
            if m == "1":
                less = methods.rectangle.calc_left(f, a, b, n)
                n *= 2
                curr = methods.rectangle.calc_left(f, a, b, n)
                while validation.runge_checker.check_runge(less, curr, 2) > e:
                    n *= 2
                    less = curr
                    curr = methods.rectangle.calc_left(f, a, b, n)
                print(f'\nЗначение: {curr}\nЧисло разбиения интервала: {n}')
            if m == "2":
                less = methods.rectangle.calc_mid(f, a, b, n)
                n *= 2
                curr = methods.rectangle.calc_mid(f, a, b, n)
                while validation.runge_checker.check_runge(less, curr, 2) > e:
                    n *= 2
                    less = curr
                    curr = methods.rectangle.calc_mid(f, a, b, n)
                print(f'\nЗначение: {curr}\nЧисло разбиения интервала: {n}')
            if m == "3":
                less = methods.rectangle.calc_right(f, a, b, n)
                n *= 2
                curr = methods.rectangle.calc_right(f, a, b, n)
                while validation.runge_checker.check_runge(less, curr, 2) > e:
                    n *= 2
                    less = curr
                    curr = methods.rectangle.calc_right(f, a, b, n)
                print(f'\nЗначение: {curr}\nЧисло разбиения интервала: {n}')
            if m == "4":
                less = methods.trapez.calc_trapez(f, a, b, n)
                n *= 2
                curr = methods.trapez.calc_trapez(f, a, b, n)
                while validation.runge_checker.check_runge(less, curr, 2) > e:
                    n *= 2
                    less = curr
                    curr = methods.trapez.calc_trapez(f, a, b, n)
                print(f'\nЗначение: {curr}\nЧисло разбиения интервала: {n}')
            if m == "5":
                less = methods.simpson.calc_simpson(f, a, b, n)
                n *= 2
                curr = methods.simpson.calc_simpson(f, a, b, n)
                while validation.runge_checker.check_runge(less, curr, 4) > e:
                    n *= 2
                    less = curr
                    curr = methods.simpson.calc_simpson(f, a, b, n)
                print(f'\nЗначение: {curr}\nЧисло разбиения интервала: {n}')
    except EOFError:
        print("Завершаем выполнение программы.")
        sys.exit(0)


if __name__ == '__main__':
    start()


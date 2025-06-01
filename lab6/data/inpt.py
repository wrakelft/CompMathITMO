import sys
import data.validator


def from_keyboard(f):
    while True:
        try:
            x0, xn = map(float, input("Введите интервал через пробел: ").replace(',', '.').split())
            if f == "2" and x0 == 0:
                print("Для этого уравнения x0 не может быть 0")
                raise ValueError
            elif not data.validator.validate_interval(x0, xn):
                print("Левая граница не может быть меньше или равна правой!")
                raise ValueError
            y0 = float(input(f"Введите начальное значение y(x0) = y({x0}):").replace(',', '.'))
            h = float(input("Введите шаг h > 0: ").replace(',', '.'))
            if not data.validator.validate_h(h, x0, xn):
                print("Шаг должен быть положительным и меньше интервала")
                raise ValueError
            e = float(input("Введите точность системы >0 и <1: ").replace(',', '.'))
            if not data.validator.validate_eps(e):
                print("Точность не может быть меньше 0 или больше 1")
                raise ValueError
            return x0, xn, y0, h, e
        except ValueError:
            print("Вводите числа! Для интервала два через пробел, "
                  "для y0, шага и точности только одно!")
        except EOFError:
            print("Завершаем выполнение программы.")
            sys.exit(0)

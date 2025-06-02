import numpy as np
import sys
import validator


def check_input_data(x, y):
    if len(x) == 0 or len(y) == 0:
        raise ValueError("Таблица не может быть пустой!")
    if np.all(x == 0) or np.all(y == 0):
        raise ValueError("Все значения x или y равны нулю")
    if len(np.unique(x)) != len(x) or len(np.unique(y)) != len(y):
        raise ValueError("Среди x y есть не уникальные числа")


def from_keyboard():
    try:
        x = []
        y = []
        print("Введите точку интерполяции:")
        x_interp = float(input().replace(',', '.'))
        print("Вводите по две пары чисел на каждой строке (X Y)")
        print("Для завершения ввода оставьте строку пустой")
        while True:
            inp = input()
            point = inp.strip().split()
            if not inp:
                break
            if len(point) == 2:
                x.append(float(point[0].replace(',', '.')))
                y.append(float(point[1].replace(',', '.')))
            else:
                raise ValueError
        if not x:
            raise ValueError("Таблица не введена!")
        if x_interp < min(x) or x_interp > max(x):
            print(f"Точка интерполяции должна быть между {min(x)} и {max(x)}")
            sys.exit(1)
        x = np.array(x)
        y = np.array(y)
        check_input_data(x, y)
        return x, y, x_interp
    except ValueError as e:
        print(e)
        print("Вводите числа! X Y - два числа в одной строке через пробел, точка инетрп. одно число")
        sys.exit(1)
    except EOFError:
        print("Завершаем выполнение программы.")
        sys.exit(0)


def from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as fi:
            lines = []
            for line in fi:
                strp = line.strip()
                if strp:
                    lines.append(strp)
            x = []
            y = []
            for i, line in enumerate(lines, 1):
                parts = line.replace(',', '.').split()
                if len(parts) != 2:
                    print(f"Ошибка в строке {i}, ожидается 2 числа, получено {len(parts)}")
                    sys.exit(1)
                x.append(float(parts[0]))
                y.append(float(parts[1]))
            if not x:
                print("Файл пуст или не содержит корректных данных")
                sys.exit(1)
            x = np.array(x)
            y = np.array(y)
            check_input_data(x, y)
            return x, y
    except ValueError as e:
        print(e)
        print("Вводите в файле числа! Xi Yi - два в одной строке через пробел")
        sys.exit(1)
    except EOFError:
        print("Завершаем выполнение программы.")
        sys.exit(0)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден!")
        sys.exit(1)
    except PermissionError:
        print(f"Нет доступа к файлу '{filename}'!")
        sys.exit(1)


def user():
    try:
        f = ""
        while f != "1" and f != "2":
            f = input("Выберите уравнение: \n" + "1. y = sin(x)\n2. y = cos(x)\n" + "\n")
        if f == "1" or f == "2":
            a, b = map(float, input("Введите интервал через пробел: ").replace(',', '.').split())
            if not validator.validate_interval(a, b):
                print("Левая граница не может быть меньше или равна правой!")
                sys.exit(1)
            n = int(input("Введите количество точек: "))
            if n <= 0:
                print("Кол-во точек должно быть > 0")
                sys.exit(1)

            x = np.linspace(a, b, n)
            if f == "1":
                y = np.sin(x)
            else:
                y = np.cos(x)
            xim = float(input('Введите точку интерполяции: ').replace(',', '.'))
            if xim < a or xim > b:
                print("Точка должна лежать на интервале или быть среди точек определнный в x с учетом h!")
                sys.exit(1)

            return x, y, xim
    except ValueError:
        print("Вводите числа! Для интервала два через пробел (первое < второе), для точки интерп. только одно!")
        sys.exit(1)
    except EOFError:
        print("Завершаем выполнение программы.")
        sys.exit(0)

import sys
import numpy as np


def check_input_data(x, y):
    if np.all(x == 0) or np.all(y == 0):
        raise ValueError("Все значения x или y равны нулю")
    if len(np.unique(x)) != len(x) or len(np.unique(y)) != len(y):
        raise ValueError("Среди x y есть неуникальные числа")


def from_keyboard():
    while True:
        try:
            p = int(input("Введите кол-во точек от 8 до 12: "))
            if p < 8 or p > 12:
                print("Кол-во точек должно быть целым числом меньше 8 или больше 12")
                raise ValueError
            x = []
            y = []
            print("Вводите по две пары чисел на каждой строке (Xi Yi)")
            for i in range(p):
                inp = input()
                point = inp.strip().split()
                if len(point) == 2:
                    x.append(float(point[0].replace(',', '.')))
                    y.append(float(point[1].replace(',', '.')))
                else:
                    raise ValueError
            if len(x) != p or len(y) != p:
                print("Не совпадает кол-во точек")
                sys.exit(0)
            x = np.array(x)
            y = np.array(y)
            check_input_data(x, y)
            return x, y, p
        except ValueError as e:
            print(e)
            print("Вводите числа! Xi Yi - два в одной строке через пробел, кол-во точек одно целое число")
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
            p = len(lines)
            if p < 8 or p > 12:
                print("Неверная структура данных в файле!")
                sys.exit(1)
            x = []
            y = []
            for i, line in enumerate(lines, 1):
                parts = line.replace(',', '.').split()
                if len(parts) != 2:
                    print(f"Ошибка в строке {i}, ожидается 2 числа, получено {len(parts)}")
                    sys.exit(1)
                x.append(float(parts[0]))
                y.append(float(parts[1]))
            x = np.array(x)
            y = np.array(y)
            check_input_data(x, y)
            return x, y, p
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




import inpt
import sys
import functions.diff
import functions.Lagranj
import functions.Newton_raz
import functions.Newton_kon
import graph


def start():
    try:
        i = ""
        while i != "a" and i != "b" and i != "c":
            i = input("Выберите способ ввода: клавиатура - a, файл - b, на основе функций - с: ").strip()
        if i == "a":
            x, y, xim = inpt.from_keyboard()
            dif_t = functions.diff.diff_table(x, y)
            res_l = functions.Lagranj.lagrange_calc(x, y, xim)
            res_nk = functions.Newton_kon.newton_kon_calc(x, y, dif_t, xim)
            res_nr = functions.Newton_raz.newton_raz_calc(x, y, xim)
            if res_nk == 0:
                print(f"\nРезультаты: \nЛангранж: {res_l} \nНьютон с конечными разностями: шаг должен быть равномерный"
                    f"\nНьютон с раздельными разностями: {res_nr}")
            else:
                functions.diff.print_diff_table(dif_t)
                print(f"\nРезультаты: \nЛангранж: {res_l} \nНьютон с конечными разностями: {res_nk} "
                      f"\nНьютон с раздельными разностями: {res_nr}")
            if len(y) % 2 == 0:
                print("\nФормула Стирлинга требует нечетного числа узлов")
            else:
                print("\nФормула Бесселя требует четного числа узлов")
            graph.plot_all_methods(x, y, dif_t, xim)
        elif i == "b":
            filename = input("Введите имя файла: ").strip()
            x, y = inpt.from_file(filename)
            print("Введите точку интерполяции:")
            xim = float(input().replace(',', '.'))
            if xim < min(x) or xim > max(x):
                print(f"Точка интерполяции должна быть между {min(x)} и {max(x)}")
                sys.exit(1)
            dif_t = functions.diff.diff_table(x, y)
            res_l = functions.Lagranj.lagrange_calc(x, y, xim)
            res_nk = functions.Newton_kon.newton_kon_calc(x, y, dif_t, xim)
            res_nr = functions.Newton_raz.newton_raz_calc(x, y, xim)
            if res_nk == 0:
                print(f"\nРезультаты: \nЛангранж: {res_l} \nНьютон с конечными разностями: шаг должен быть равномерный"
                    f"\nНьютон с раздельными разностями: {res_nr}")
            else:
                functions.diff.print_diff_table(dif_t)
                print(f"\nРезультаты: \nЛангранж: {res_l} \nНьютон с конечными разностями: {res_nk} "
                      f"\nНьютон с раздельными разностями: {res_nr}")
            if len(y) % 2 == 0:
                print("\nФормула Стирлинга требует нечетного числа узлов")
            else:
                print("\nФормула Бесселя требует четного числа узлов")
            graph.plot_all_methods(x, y, dif_t, xim)
        elif i == "c":
            x, y, xim = inpt.user()
            dif_t = functions.diff.diff_table(x, y)
            res_l = functions.Lagranj.lagrange_calc(x, y, xim)
            res_nk = functions.Newton_kon.newton_kon_calc(x, y, dif_t, xim)
            res_nr = functions.Newton_raz.newton_raz_calc(x, y, xim)
            if res_nk == 0:
                print(f"\nРезультаты: \nЛангранж: {res_l} \nНьютон с конечными разностями: шаг должен быть равномерный"
                      f"\nНьютон с раздельными разностями: {res_nr}")
            else:
                functions.diff.print_diff_table(dif_t)
                print(f"\nРезультаты: \nЛангранж: {res_l} \nНьютон с конечными разностями: {res_nk} "
                      f"\nНьютон с раздельными разностями: {res_nr}")
            if len(y) % 2 == 0:
                print("\nФормула Стирлинга требует нечетного числа узлов")
            else:
                print("\nФормула Бесселя требует четного числа узлов")
            graph.plot_all_methods(x, y, dif_t, xim)
    except ValueError:
        print("Вводите числа! Для точки интерп. только одно!")
        sys.exit(1)
    except EOFError:
        print("Завершаем выполнение программы.")
        sys.exit(0)


if __name__ == "__main__":
    start()

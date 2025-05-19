import functions.linear
import functions.exponential
import functions.logarithmic
import functions.power
import inpt
import prepocess
import numpy as np
import outpt
import sys
import graph

prepocess.preprocess("functions/rus/полином2СТ.py", "functions/полином2СТ.py")
prepocess.preprocess("functions/rus/полином3СТ.py", "functions/полином3СТ.py")
files_to_remove = ["functions/полином2СТ.py", "functions/полином3СТ.py"]

from functions.полином2СТ import посчитать_полиномСТ2
from functions.полином3СТ import посчитать_полиномСТ3


def start():
    try:
        inp = ""
        while inp != "f" and inp != "k":
            inp = input("Выберите откуда ввести начальный набор точек, f - из файла, k - с клавиатуры: ")
        if inp == "k":
            x, y, p = inpt.from_keyboard()
            model_results = {}
        else:
            print("Файл должен содержать от 8 до 12 пар точек, по две на каждой строке через пробел")
            filename = input("Введите имя файла: ").strip()
            x, y, p = inpt.from_file(filename)
            model_results = {}
        out = ""
        while out != "f" and out != "s":
            out = input("Выберите куда вывести результат работы программы, f - в файл, s - на экран: ")
        if out == "s":
            if np.all(x > 0):
                if np.all(y > 0):
                    a, b, n, e, s_l, q_l, R, r = functions.linear.calc_linear(x, y, p)
                    outpt.print_model_results("Линейная", x, y, n, a, b, 0, 0, s_l, e, q_l, R, r)
                    model_results['Линейная'] = {
                        'name': 'Линейная',
                        'coeffs': [a, b],
                        'R^2': R
                    }

                    a, b, c, n, e, s_p2, q_p2, R = functions.полином2СТ.посчитать_полиномСТ2(x, y, p)
                    outpt.print_model_results("Полином 2-ст", x, y, n, a, b, c, 0, s_p2, e, q_p2, R)
                    model_results['Полином2СТ'] = {
                        'name': 'Полином 2-ст',
                        'coeffs': [a, b, c],
                        'R^2': R
                    }

                    a, b, c, d, n, e, s_p3, q_p3, R = functions.полином3СТ.посчитать_полиномСТ3(x, y, p)
                    outpt.print_model_results("Полином 3-ст", x, y, n, a, b, c, d, s_p3, e, q_p3, R)
                    model_results['Полином3СТ'] = {
                        'name': 'Полином 3-ст',
                        'coeffs': [a, b, c, d],
                        'R^2': R
                    }

                    a, b, n, e, s_e, q_e, R = functions.exponential.calc_exponential(x, y, p)
                    outpt.print_model_results("Экспоненциальная", x, y, n, a, b, 0, 0, s_e, e, q_e, R)
                    model_results['Экспоненциальная'] = {
                        'name': 'Экспоненциальная',
                        'coeffs': [a, b],
                        'R^2': R
                    }

                    a, b, n, e, s_log, q_log, R = functions.logarithmic.calc_logarithmic(x, y, p)
                    outpt.print_model_results("Логарифмическая", x, y, n, a, b, 0, 0, s_log, e, q_log, R)
                    model_results['Логарифмическая'] = {
                        'name': 'Логарифмическая',
                        'coeffs': [a, b],
                        'R^2': R
                    }

                    a, b, n, e, s_st, q_st, R = functions.power.calc_power(x, y, p)
                    outpt.print_model_results("Степенная", x, y, n, a, b, 0, 0, s_st, e, q_st, R)
                    model_results['Степенная'] = {
                        'name': 'Степенная',
                        'coeffs': [a, b],
                        'R^2': R
                    }
                    outpt.print_best_model(q_l, q_p2, q_p3, q_e, q_log, q_st)
                    graph.plot_all_functions(x, y, model_results)
                    print("Закройте окно с показом функций, чтобы завершить программу")
                    prepocess.clean(files_to_remove)
                else:
                    a, b, n, e, s_l, q_l, R, r = functions.linear.calc_linear(x, y, p)
                    outpt.print_model_results("Линейная", x, y, n, a, b, 0, 0, s_l, e, q_l, R, r)
                    model_results['Линейная'] = {
                        'name': 'Линейная',
                        'coeffs': [a, b],
                        'R^2': R
                    }

                    a, b, c, n, e, s_p2, q_p2, R = functions.полином2СТ.посчитать_полиномСТ2(x, y, p)
                    outpt.print_model_results("Полином 2-ст", x, y, n, a, b, c, 0, s_p2, e, q_p2, R)
                    model_results['Полином2СТ'] = {
                        'name': 'Полином 2-ст',
                        'coeffs': [a, b, c],
                        'R^2': R
                    }

                    a, b, c, d, n, e, s_p3, q_p3, R = functions.полином3СТ.посчитать_полиномСТ3(x, y, p)
                    outpt.print_model_results("Полином 3-ст", x, y, n, a, b, c, d, s_p3, e, q_p3, R)
                    model_results['Полином3СТ'] = {
                        'name': 'Полином 3-ст',
                        'coeffs': [a, b, c, d],
                        'R^2': R
                    }

                    a, b, n, e, s_log, q_log, R = functions.logarithmic.calc_logarithmic(x, y, p)
                    outpt.print_model_results("Логарифмическая", x, y, n, a, b, 0, 0, s_log, e, q_log, R)
                    model_results['Логарифмическая'] = {
                        'name': 'Логарифмическая',
                        'coeffs': [a, b],
                        'R^2': R
                    }
                    outpt.print_best_model(q_l, q_p2, q_p3, 1000, q_log, 1000)
                    graph.plot_all_functions(x, y, model_results)
                    print("Закройте окно с показом функций, чтобы завершить программу")
                    prepocess.clean(files_to_remove)
            else:
                if np.all(y > 0):
                    a, b, n, e, s_l, q_l, R, r = functions.linear.calc_linear(x, y, p)
                    outpt.print_model_results("Линейная", x, y, n, a, b, 0, 0, s_l, e, q_l, R, r)
                    model_results['Линейная'] = {
                        'name': 'Линейная',
                        'coeffs': [a, b],
                        'R^2': R
                    }

                    a, b, c, n, e, s_p2, q_p2, R = functions.полином2СТ.посчитать_полиномСТ2(x, y, p)
                    outpt.print_model_results("Полином 2-ст", x, y, n, a, b, c, 0, s_p2, e, q_p2, R)
                    model_results['Полином2СТ'] = {
                        'name': 'Полином 2-ст',
                        'coeffs': [a, b, c],
                        'R^2': R
                    }

                    a, b, c, d, n, e, s_p3, q_p3, R = functions.полином3СТ.посчитать_полиномСТ3(x, y, p)
                    outpt.print_model_results("Полином 3-ст", x, y, n, a, b, c, d, s_p3, e, q_p3, R)
                    model_results['Полином3СТ'] = {
                        'name': 'Полином 3-ст',
                        'coeffs': [a, b, c, d],
                        'R^2': R
                    }

                    a, b, n, e, s_e, q_e, R = functions.exponential.calc_exponential(x, y, p)
                    outpt.print_model_results("Экспоненциальная", x, y, n, a, b, 0, 0, s_e, e, q_e, R)
                    model_results['Экспоненциальная'] = {
                        'name': 'Экспоненциальная',
                        'coeffs': [a, b],
                        'R^2': R
                    }
                    outpt.print_best_model(q_l, q_p2, q_p3, q_e, 1000, 1000)
                    graph.plot_all_functions(x, y, model_results)
                    print("Закройте окно с показом функций, чтобы завершить программу")
                    prepocess.clean(files_to_remove)
                else:
                    a, b, n, e, s_l, q_l, R, r = functions.linear.calc_linear(x, y, p)
                    outpt.print_model_results("Линейная", x, y, n, a, b, 0, 0, s_l, e, q_l, R, r)
                    model_results['Линейная'] = {
                        'name': 'Линейная',
                        'coeffs': [a, b],
                        'R^2': R
                    }

                    a, b, c, n, e, s_p2, q_p2, R = functions.полином2СТ.посчитать_полиномСТ2(x, y, p)
                    outpt.print_model_results("Полином 2-ст", x, y, n, a, b, c, 0, s_p2, e, q_p2, R)
                    model_results['Полином2СТ'] = {
                        'name': 'Полином 2-ст',
                        'coeffs': [a, b, c],
                        'R^2': R
                    }

                    a, b, c, d, n, e, s_p3, q_p3, R = functions.полином3СТ.посчитать_полиномСТ3(x, y, p)
                    outpt.print_model_results("Полином 3-ст", x, y, n, a, b, c, d, s_p3, e, q_p3, R)
                    model_results['Полином3СТ'] = {
                        'name': 'Полином 3-ст',
                        'coeffs': [a, b, c, d],
                        'R^2': R
                    }
                    outpt.print_best_model(q_l, q_p2, q_p3, 1000, 1000, 1000)
                    graph.plot_all_functions(x, y, model_results)
                    print("Закройте окно с показом функций, чтобы завершить программу")
                    prepocess.clean(files_to_remove)
        else:
            res = ""
            i_res = ""
            if np.all(x > 0):
                if np.all(y > 0):
                    a, b, n, e, s_l, q_l, R, r = functions.linear.calc_linear(x, y, p)
                    i_res = outpt.form_output_main("Линейная", x, y, n, a, b, 0, 0, s_l, e, q_l, R, i_res, r)
                    model_results['Линейная'] = {
                        'name': 'Линейная',
                        'coeffs': [a, b],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""

                    a, b, c, n, e, s_p2, q_p2, R = functions.полином2СТ.посчитать_полиномСТ2(x, y, p)
                    i_res = outpt.form_output_main("Полином 2-ст", x, y, n, a, b, c, 0, s_p2, e, q_p2, R, i_res)
                    model_results['Полином2СТ'] = {
                        'name': 'Полином 2-ст',
                        'coeffs': [a, b, c],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""

                    a, b, c, d, n, e, s_p3, q_p3, R = functions.полином3СТ.посчитать_полиномСТ3(x, y, p)
                    i_res = outpt.form_output_main("Полином 3-ст", x, y, n, a, b, c, d, s_p3, e, q_p3, R, i_res)
                    model_results['Полином3СТ'] = {
                        'name': 'Полином 3-ст',
                        'coeffs': [a, b, c, d],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""

                    a, b, n, e, s_e, q_e, R = functions.exponential.calc_exponential(x, y, p)
                    i_res = outpt.form_output_main("Экспоненциальная", x, y, n, a, b, 0, 0, s_e, e, q_e, R, i_res)
                    model_results['Экспоненциальная'] = {
                        'name': 'Экспоненциальная',
                        'coeffs': [a, b],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""

                    a, b, n, e, s_log, q_log, R = functions.logarithmic.calc_logarithmic(x, y, p)
                    i_res = outpt.form_output_main("Логарифмическая", x, y, n, a, b, 0, 0, s_log, e, q_log, R, i_res)
                    model_results['Логарифмическая'] = {
                        'name': 'Логарифмическая',
                        'coeffs': [a, b],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""

                    a, b, n, e, s_st, q_st, R = functions.power.calc_power(x, y, p)
                    i_res = outpt.form_output_main("Степенная", x, y, n, a, b, 0, 0, s_st, e, q_st, R, i_res)
                    model_results['Степенная'] = {
                        'name': 'Степенная',
                        'coeffs': [a, b],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""
                    i_res = outpt.form_best_model(q_l, q_p2, q_p3, q_e, q_log, q_st, i_res)
                    res += i_res
                    outpt.save_file(res)
                    graph.plot_all_functions(x, y, model_results)
                    print("Закройте окно с показом функций, чтобы завершить программу")
                    prepocess.clean(files_to_remove)
                else:
                    a, b, n, e, s_l, q_l, R, r = functions.linear.calc_linear(x, y, p)
                    i_res = outpt.form_output_main("Линейная", x, y, n, a, b, 0, 0, s_l, e, q_l, R, i_res, r)
                    model_results['Линейная'] = {
                        'name': 'Линейная',
                        'coeffs': [a, b],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""

                    a, b, c, n, e, s_p2, q_p2, R = functions.полином2СТ.посчитать_полиномСТ2(x, y, p)
                    i_res = outpt.form_output_main("Полином 2-ст", x, y, n, a, b, c, 0, s_p2, e, q_p2, R, i_res)
                    model_results['Полином2СТ'] = {
                        'name': 'Полином 2-ст',
                        'coeffs': [a, b, c],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""

                    a, b, c, d, n, e, s_p3, q_p3, R = functions.полином3СТ.посчитать_полиномСТ3(x, y, p)
                    i_res = outpt.form_output_main("Полином 3-ст", x, y, n, a, b, c, d, s_p3, e, q_p3, R, i_res)
                    model_results['Полином3СТ'] = {
                        'name': 'Полином 3-ст',
                        'coeffs': [a, b, c, d],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""

                    a, b, n, e, s_log, q_log, R = functions.logarithmic.calc_logarithmic(x, y, p)
                    i_res = outpt.form_output_main("Логарифмическая", x, y, n, a, b, 0, 0, s_log, e, q_log, R, i_res)
                    model_results['Логарифмическая'] = {
                        'name': 'Логарифмическая',
                        'coeffs': [a, b],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""
                    i_res = outpt.form_best_model(q_l, q_p2, q_p3, 1000, q_log, 1000, i_res)
                    res += i_res
                    outpt.save_file(res)
                    graph.plot_all_functions(x, y, model_results)
                    print("Закройте окно с показом функций, чтобы завершить программу")
                    prepocess.clean(files_to_remove)
            else:
                if np.all(y > 0):
                    a, b, n, e, s_l, q_l, R, r = functions.linear.calc_linear(x, y, p)
                    i_res = outpt.form_output_main("Линейная", x, y, n, a, b, 0, 0, s_l, e, q_l, R, i_res, r)
                    model_results['Линейная'] = {
                        'name': 'Линейная',
                        'coeffs': [a, b],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""

                    a, b, c, n, e, s_p2, q_p2, R = functions.полином2СТ.посчитать_полиномСТ2(x, y, p)
                    i_res = outpt.form_output_main("Полином 2-ст", x, y, n, a, b, c, 0, s_p2, e, q_p2, R, i_res)
                    model_results['Полином2СТ'] = {
                        'name': 'Полином 2-ст',
                        'coeffs': [a, b, c],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""

                    a, b, c, d, n, e, s_p3, q_p3, R = functions.полином3СТ.посчитать_полиномСТ3(x, y, p)
                    i_res = outpt.form_output_main("Полином 3-ст", x, y, n, a, b, c, d, s_p3, e, q_p3, R, i_res)
                    model_results['Полином3СТ'] = {
                        'name': 'Полином 3-ст',
                        'coeffs': [a, b, c, d],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""

                    a, b, n, e, s_e, q_e, R = functions.exponential.calc_exponential(x, y, p)
                    i_res = outpt.form_output_main("Экспоненциальная", x, y, n, a, b, 0, 0, s_e, e, q_e, R, i_res)
                    model_results['Экспоненциальная'] = {
                        'name': 'Экспоненциальная',
                        'coeffs': [a, b],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""
                    i_res = outpt.form_best_model(q_l, q_p2, q_p3, q_e, 1000, 1000, i_res)
                    res += i_res
                    outpt.save_file(res)
                    graph.plot_all_functions(x, y, model_results)
                    print("Закройте окно с показом функций, чтобы завершить программу")
                    prepocess.clean(files_to_remove)
                else:
                    a, b, n, e, s_l, q_l, R, r = functions.linear.calc_linear(x, y, p)
                    i_res = outpt.form_output_main("Линейная", x, y, n, a, b, 0, 0, s_l, e, q_l, R, i_res, r)
                    model_results['Линейная'] = {
                        'name': 'Линейная',
                        'coeffs': [a, b],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""

                    a, b, c, n, e, s_p2, q_p2, R = functions.полином2СТ.посчитать_полиномСТ2(x, y, p)
                    i_res = outpt.form_output_main("Полином 2-ст", x, y, n, a, b, c, 0, s_p2, e, q_p2, R, i_res)
                    model_results['Полином2СТ'] = {
                        'name': 'Полином 2-ст',
                        'coeffs': [a, b, c],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""

                    a, b, c, d, n, e, s_p3, q_p3, R = functions.полином3СТ.посчитать_полиномСТ3(x, y, p)
                    i_res = outpt.form_output_main("Полином 3-ст", x, y, n, a, b, c, d, s_p3, e, q_p3, R, i_res)
                    model_results['Полином3СТ'] = {
                        'name': 'Полином 3-ст',
                        'coeffs': [a, b, c, d],
                        'R^2': R
                    }
                    res += i_res
                    i_res = ""
                    i_res = outpt.form_best_model(q_l, q_p2, q_p3, 1000, 1000, 1000, i_res)
                    res += i_res
                    outpt.save_file(res)
                    graph.plot_all_functions(x, y, model_results)
                    print("Закройте окно с показом функций, чтобы завершить программу")
                    prepocess.clean(files_to_remove)
    except EOFError:
        print("Завершаем выполнение программы.")
        sys.exit(0)


if __name__ == '__main__':
    start()


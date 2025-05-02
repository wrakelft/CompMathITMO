import additional_functions.derivative
import properties.properties
import tasks.task


def calc_newton(f, x, e):
    func = tasks.task.get_function(f)
    df = additional_functions.derivative.fabric_df(func)

    x0 = x
    for i in range(properties.properties.max_iter):
        fx = func(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Производная равна нулю!")
            return 0, 0, 0
        x_next = x0 - fx/dfx

        if abs(x_next - x0) <= e:
            return x_next, func(x_next), i + 1

        x0 = x_next

    return 0, 0, properties.properties.max_iter
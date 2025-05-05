from enum import Enum
import math


class Functions(Enum):
    one = ("-x^3 - x^2 - 2x + 1", lambda x: -x**3 - x**2 - 2*x + 1)
    two = ("5x^2 + 3x", lambda x: 5*x**2 + 3*x)
    three = ("cos(x) + x", lambda x: math.cos(x) + x)
    four = ("sin(x)", lambda x: math.sin(x))

    @classmethod
    def get_func_lambda(cls, name):
        return cls[name].value[1]

    @classmethod
    def get_func_string(cls, name):
        return cls[name].value[0]

    @classmethod
    def show_all_func(cls):
        return ("1. " + Functions.one.value[0] + "\n" + "2. " + Functions.two.value[0] + "\n"
                + "3. " + Functions.three.value[0] + "\n" + "4. " + Functions.four.value[0] + "\n")


import inpt
import functions.linear as linear
import functions.exponential as expn
import functions.logarithmic as loga
import functions.power as power


def start():
    x, y = inpt.from_file("test.txt")
    a, b = power.calc_power(x, y)
    print(a, b)


if __name__ == '__main__':
    start()
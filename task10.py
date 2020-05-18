#дз  Сделайте бенчмарк двух функций, в каждой из которых одна и та же цель:
# принимает на вход число и возвращает список чисел во второй, третье, четвертой и 5 степени.
# Одна функция делает это с помощью рекурсии, другая с помощью цикла. В результате бенчмарк сдавать в виде графика.

from simple_benchmark import benchmark, MultiArgument
import matplotlib.pyplot as plt


def get_degree_c(x):
    res = []
    for i in range(2, 6):
        res.append(x**i)
    return res


def get_degree(x, de):
    if de == 2:
        return [x**de]
    else:
        res = get_degree(x, de-1)
        res.append(x**de)
        return res


def get_degree_r(x):
    return get_degree(x, 5)


func = [get_degree_c, get_degree_r]
arguments = {}
for i in range(50):
    arguments['i' + str(i)] = i
print(arguments)
arguments_name = 'natural numbers'

aliases = {get_degree_c: "Циклическая функция", get_degree_r: "Рекурсия"}
b = benchmark(func, arguments, arguments_name, function_aliases=aliases)
b.plot()
plt.show(b)


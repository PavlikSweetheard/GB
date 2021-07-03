# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def stepen(x, y):
    try:
        x, y = float(x), int(y)
        return x ** y
    except ValueError:
        return "Некорректные данные"


def stepen_var_2(x, y):
    try:
        x, y = float(x), int(y)
        rez = x
        for i in range(abs(y) - 1):
            rez = rez * x
        return 1 / rez
    except ValueError:
        return "Некорректные данные"


x = input("Введите число (дейстивтельное положительно число):")
y = input("Введите степень ( целове отрицательное число):")

print(stepen(x, y))
print(stepen_var_2(x, y))

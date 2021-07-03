# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def del_2(arg_1, arg_2):
    try:
        arg_1, arg_2 = float(arg_1), float(arg_2)
        rez = arg_1 / arg_2
    except ValueError:
        return "Числа введены некорректно!"
    except ZeroDivisionError:
        return "Деление на ноль недопустимо!"
    return rez


print(del_2(10, 0))

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    try:
        arg_1, arg_2, arg_3 = float(arg_1), float(arg_2), float(arg_3)
        my_list = [arg_1, arg_2, arg_3]
        my_list.remove(min(my_list))
        return "сумма двух наибольших : " + str(sum(my_list))
    except ValueError:
        return "Аргументы введнеы неправильно"


print(my_func(
    input("Ввелите первое число:"),
    input("Ввелите второе число:"),
    input("Ввелите третье число:"),
))

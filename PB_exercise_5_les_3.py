# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def summa():
    exit_simbol = False
    rezult = 0
    while exit_simbol == False:
        el_list = input("Введите строку (для выхода введите знак '$'): ").split()
        summ_line = 0
        for el in el_list:
            if "$" in el:
                exit_simbol = True
                break
            summ_line += float(el)
        rezult += summ_line
        print(rezult)

summa()













# def summ(stroka):
#     args_list = stroka.split()
#     sum = 0
#     for el in args_list:
#         if el == "$":
#             break
#         else:
#             sum += float(el)
#     return sum
#
#
# summa = 0
#
# while True:
#     stroka = input("Введите строку (для выхода введите знак '$'): ")
#     if "$" in stroka:
#         summa += summ(stroka)
#         print("Сумма равна", summa)
#         break
#     else:
#         summa += summ(stroka)
#         print("Сумма равна", summa)

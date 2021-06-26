# 4.Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

numeric = int(input('Введите целое положительное число : \n'))

max_num = numeric % 10

while numeric > 0:
    if max_num == 9:
        break
    if numeric % 10 > max_num:
        max_num = numeric % 10
    numeric = numeric // 10

print('Наибольшая цифра у введенного числа =', max_num)

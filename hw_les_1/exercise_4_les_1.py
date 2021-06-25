# 4.Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

numeric = int(input('Введите целое положительное число : \n'))

max_num = numeric % 10

while numeric // 10 > 0:
    el = numeric % 10
    print(el)
    if max_num == 9:
        break
    if el > max_num:
        max_num = el
    numeric = numeric // 10
    print(numeric)

print(max_num, 'swef')
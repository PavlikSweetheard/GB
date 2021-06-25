# 2.Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

time = None

time = int(input('Введите время (в секундах) для дальнейшего перевода в фомат чч:мм:сс :'))

if time // 3600 > 0:
    time_str = ("0" + str(time // 3600) if time // 3600 < 10 else str(time // 3600)) + ":" + (
        "0" + str((time % 3600) // 60) if (time % 3600 // 60) < 10 else str((time % 3600) // 60)) + ":" + (
                   "0" + str(time % 60) if time % 60 < 10 else str(time % 60))
elif time // 60 > 0:
    time_str = "00" + ":" + (
        "0" + str((time % 3600) // 60) if (time % 3600 // 60) < 10 else str((time % 3600) // 60)) + ":" + (
                   "0" + str(time % 60) if time % 60 < 10 else str(time % 60))
else:
    time_str = "00" + ":" + "00" + ":" + (
        "0" + str(time % 60) if time % 60 < 10 else str(time % 60))
print(time_str)

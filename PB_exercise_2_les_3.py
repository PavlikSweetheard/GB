# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

# вариант_1
def user_info(name, surname, year, city, email, phone_number):
    return f"Имя пользователя : {name}, фамилия : {surname}, год рождения : {year}, город проживания: {city},email : {email},телефон : {phone_number}"


# вариант_2
def user_info_2(**kwargs):
    return kwargs


print(user_info_2(
    name=input('Введите свое имя: '),
    surname=input('Введите свое фамилию: '),
    year=input('Введите свой год рождения: '),
    city=input('Введите свой город проживания: '),
    email=input('Введите свой email: '),
    phone_number=input('Введите свой телефон: '),
))


print(user_info(name="Pavel", surname="Makarov", year="1992", city="Tumen", email="makarov_595@mail.ru",
                phone_number="+79222581626"))

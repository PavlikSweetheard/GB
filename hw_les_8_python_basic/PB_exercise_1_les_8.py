"""

1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


"""


class Data:
    def __init__(self, day, month, year):
        self.d_m_y = [day, month, year]

    @classmethod
    def m_1(cls, data_str):
        d, m, y = list(map(int, data_str.split("-")))
        return Data(d, m, y)

    @staticmethod
    def m_2(obj):
        val_list = [[range(1, 31)], [range(1, 12)], [range(1900, 2021)]]
        for el, num in enumerate(obj.d_m_y):
            if el not in val_list[num]:
                break
                print("Validation faild!!!")
            else:
                print("Validation is done!!!")


data_1 = "05-07-1992"
a = Data.m_1(data_1)
Data.m_2(a)

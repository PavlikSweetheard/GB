"""

2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
 Проверить работу этих методов на реальных данных.Реализовать общий подсчет расхода ткани.
 Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
 проверить на практике работу декоратора @property.


"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    consumption_all = 0

    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        self.consumption_all += self.consumption_of_textile + other.consumption_of_textile
        return self.consumption_all

    @property
    @abstractmethod
    def consumption_of_textile(self):
        pass


class Coat(Clothes):
    @property
    def consumption_of_textile(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    @property
    def consumption_of_textile(self):
        return self.size * 2 + 0.3


coat_1 = Coat(55)
suit_1 = Suit(180)

print(coat_1.consumption_of_textile)
print(suit_1.consumption_of_textile)
print(coat_1 + suit_1)

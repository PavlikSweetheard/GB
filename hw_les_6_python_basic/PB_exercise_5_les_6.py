"""

5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
 В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить
 уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


"""


class Stationery:
    def __init__(self, stationery_title="something"):
        self.title = stationery_title

    def draw(self):
        print(f"start drawing with {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"start drawing with {self.title} ...")


class Pencil(Stationery):
    def draw(self):
        print(f"start drawing with {self.title} ...")


class Handle(Stationery):
    def draw(self):
        print(f"start drawing with {self.title} ...")



pen_1 = Pen('My pen')
pencil_1 = Pencil('My pencil')
handle_1 = Handle('My handle')

pen_1.draw()
pencil_1.draw()
handle_1.draw()
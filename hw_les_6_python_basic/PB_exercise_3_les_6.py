"""

3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность)
на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


"""


class Worker:
    def __init__(self, worker_name, worker_surname, worker_position, worker_wage, worker_bonus):
        self.name = worker_name
        self.surname = worker_surname
        self.position = worker_position
        self._income = {"wage": worker_wage, "bonus": worker_bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Full name: {self.name} {self.surname} {self.position}")

    def get_total_income(self):
        print(f"Income with bonus: {sum(self._income.values())}")


II_senior = Position('Ivan', 'Ivanov', 'senior', 150000, 500000)
II_senior.get_total_income()
II_senior.get_full_name()
print(II_senior.position)

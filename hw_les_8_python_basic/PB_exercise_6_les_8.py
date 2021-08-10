"""

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.


"""


class WarehouseOfficeEquipment:
    def __init__(self):
        self._status_warehouse = {"Printer": 0, "Scanner": 0, "Xerox": 0}

    def add_equipment(self, *objs):
        for obj in objs:
            self._status_warehouse[obj.__class__.__name__] += 1
            print("Передано на склад : ", obj.name)
        print("Всего на складе : ", warehouse._status_warehouse)

    def hand_over_to_department(self, name_of_dep, *objs):
        for obj in objs:
            self._status_warehouse[obj.__class__.__name__] -= 1
            obj.department = name_of_dep
            print(f"В отдел {name_of_dep.name} передана техника: {obj.name} ( {obj.__class__.__name__} )")
            name_of_dep._status_warehouse[obj.__class__.__name__] += 1
        print("Осталось на складе : ", self._status_warehouse)


class Department(WarehouseOfficeEquipment):
    def __init__(self, name):
        super().__init__()
        self.name = name


class OfficeEquipment:
    def __init__(self, name, made_from, dep=None):
        self.name = name
        self.made_from = made_from
        self.department = dep


class Printer(OfficeEquipment):
    def __init__(self, name, made_from, color=False):
        super().__init__(name, made_from)
        self.color = color

    def action(self):
        return "Printing"


class Scanner(OfficeEquipment):
    def __init__(self, name, made_from, speed_scaning=None):
        super().__init__(name, made_from)
        self.speed_scaning = speed_scaning

    def action(self):
        return "Scanning"


class Xerox(OfficeEquipment):
    def __init__(self, name, made_from, color=None):
        super().__init__(name, made_from)
        self.color = color

    def action(self):
        return "Xeroxing"


warehouse = WarehouseOfficeEquipment()
a1 = Xerox("name_a1", "Russia")
a2 = Xerox("name_a2", "Gernmany")
a3 = Xerox("name_a3", "USA")

b1 = Scanner("name_b1", "Russia")
b2 = Scanner("name_b2", "Gernmany")

c1 = Printer("name_c1", "Monako", True)
c2 = Printer("name_c2", "USA")
c3 = Printer("name_c2", "USA")

Dep_1 = Department("UR")
Dep_2 = Department("UPR")
Dep_3 = Department("Tsits")

warehouse.add_equipment(a1, a2, a3, b1, b2, c1, c2, c3)

warehouse.hand_over_to_department(Dep_1, a1, a2, c1)

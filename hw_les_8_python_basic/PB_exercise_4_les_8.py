"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы
оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class WarehouseOfficeEquipment:
    pass



class OfficeEquipment:
    def __init__(self, name, made_from):
        self.name = name
        self.made_from = made_from


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




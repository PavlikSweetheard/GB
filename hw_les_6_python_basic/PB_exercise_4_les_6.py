"""

4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
 Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
 Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
 Для классов TownCar и WorkCar переопределите метод show_speed.
 При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""


class Car:

    def __init__(self, car_speed, car_color, car_name, car_is_police):
        self.speed = car_speed
        self.color = car_color
        self.name = car_name
        self.is_police = car_is_police

    def go(self):
        print(f"Car {self.name} is starting ...")

    def stop(self):
        print(f"Car {self.name} stopped!")

    def turn(self, direction):
        print(f"Car {self.name} turn on {direction}")

    def show_speed(self):
        print(f"Current speed auto = {self.speed}")


class TownCar(Car):
    def show_speed(self, max_speed=60):
        print(f"Current speed auto = {self.speed}")
        if self.speed >= max_speed:
            print(f"PoliceCar called! Speed exceeded by {self.speed - max_speed} km/h.")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, max_speed=40):
        print(f"Current speed auto = = {self.speed}")
        if self.speed >= max_speed:
            print(f"PoliceCar called! Speed exceeded by {self.speed - max_speed} km/h.")


class PoliceCar(Car):
    def __init__(self, car_speed, car_color, car_name, car_is_police=True):
        super().__init__(car_speed, car_color, car_name, car_is_police)


town_car_1 = TownCar(85, "red", "Reno Logan", False)
town_car_1.go()
town_car_1.show_speed()
town_car_1.turn('left')
town_car_1.stop()

sport_car_1 = SportCar(185, "pink", "Lamborgini", False)
print("\n")
sport_car_1.go()
sport_car_1.show_speed()
sport_car_1.turn('right')
sport_car_1.stop()

work_car_1 = WorkCar(35, "blue", "Kamaz 800", False)
print("\n")
work_car_1.go()
work_car_1.show_speed()
work_car_1.turn('back')
work_car_1.stop()

police_car_1 = PoliceCar(885, "blue-white", "BMW X7")
print("\n")
police_car_1.go()
police_car_1.show_speed()
police_car_1.turn('curb')
police_car_1.stop()

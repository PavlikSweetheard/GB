"""

2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.

"""


class DivisionByZero(Exception):
    def __init__(self, message="Hey! Divider have not to be = 0"):
        self.message = message
        super().__init__(self.message)


while True:
    try:
        ddent = float(input("Please enter the dividend :"))
        dder = float(input("Please enter the divider :"))
        if dder == 0:
            raise DivisionByZero
        else:
            print(f"Rezult ofdivision {ddent} by {dder} is {ddent/dder}")
            break
    except ValueError:
        print('Only numbers can be divided')


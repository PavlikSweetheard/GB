"""

1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
 Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д.


"""


class Matrix:
    def __init__(self, list_matrix):
        self.matrix = list_matrix

    def __str__(self):
        line_all = ""
        for line in self.matrix:
            for el in line:
                line_all += str(el) + " "
            line_all += "\n"
        return line_all

    def __add__(self, other):
        return Matrix(map(lambda el_1, el_2: map(lambda x, y: x + y, el_1, el_2), self.matrix, other.matrix))


class Matrix_2(Matrix):

    def __str__(self):
        return '\n'.join(map(lambda el: "   ".join(map(str, el)), self.matrix)) + '\n'

    def __add__(self, other):
        new_list = []
        for num in range(len(self.matrix)):
            new_list.append(list(map(sum, zip(self.matrix[num], other.matrix[num]))))
        return new_list


ex_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ex_2 = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]

# print(Matrix(ex_1))
# print(Matrix(ex_2))
print(Matrix(ex_1) + Matrix(ex_2))

# print(Matrix_2(ex_1))
# print(Matrix_2(ex_2))
print(Matrix_2(ex_1) + Matrix_2(ex_2))

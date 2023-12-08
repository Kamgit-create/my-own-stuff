class Matrix:
    def __init__(self, matrix: list[list[int | float]]):
        if self.__is_matrix_valid(matrix):
            self.__matrix = matrix
            self.__height = len(matrix)
            self.__width = len(matrix[0])

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, new_matrix):
        if self.__is_matrix_valid(new_matrix):
            self.__matrix = new_matrix
            self.__height = len(new_matrix)
            self.__width = len(new_matrix[0])

    @staticmethod
    def __is_matrix_valid(matrix: list[list[int | float]]):
        for i in range(len(matrix) - 1):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise ValueError("Rows of matrix must be the same length")

        for row in matrix:
            for value in row:
                if not isinstance(value, int | float):
                    raise ValueError("Values of matrix must be type int or float")

        return True

    def __is_matrix_the_same_size(self, matrix: list[list[int | float]]):
        if self.__is_matrix_valid(matrix):
            return len(matrix) == self.height and len(matrix[0]) == self.width

    def __str__(self):
        string = ""

        for i in self.__matrix:
            string += " ".join([str(j) for j in i]) + "\n"

        return string.strip()

    def add(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("You can not add Matrix with anything else than another Matrix")

        if not self.__is_matrix_the_same_size(other.matrix):
            raise ValueError("Matrices must be the same size when summing")

        for i in range(len(other.matrix)):
            for j in range(len(other.matrix)):
                self.__matrix[i][j] += other.matrix[i][j]
                other.matrix[i][j] = self.__matrix[i][j]

    def subtract(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("You can not add Matrix with anything else than another Matrix")

        if not self.__is_matrix_the_same_size(other.matrix):
            raise ValueError("Matrices must be the same size when subtracting")

        for i in range(len(other.matrix)):
            for j in range(len(other.matrix)):
                self.__matrix[i][j] -= other.matrix[i][j]
                other.matrix[i][j] = self.__matrix[i][j]

    def multiply(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("You can not add Matrix with anything else than another Matrix")

        if not self.__is_matrix_the_same_size(other.matrix):
            raise ValueError("Matrices must be the same size when multiplying")

        for i in range(len(other.matrix)):
            for j in range(len(other.matrix)):
                self.__matrix[i][j] *= other.matrix[i][j]
                other.matrix[i][j] = self.__matrix[i][j]

    def transpose(self):
        new_matrix: list[list[int | float]] = [[] for _ in range(self.width)]

        for i in range(self.height):
            for j in range(self.width):
                new_matrix[j].append(self.matrix[i][j])

        self.matrix = new_matrix


m1 = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
m2 = Matrix([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])
m3 = Matrix([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Вывод матриц:")
print(m1, end="\n\n")
print(m2, end="\n\n")
print(m3, end="\n\n\n")

print("Сложение матриц")
m1.add(m2)
print(m1, end="\n\n")
print(m2, end="\n\n\n")

print("умножение матриц")
m1.multiply(m2)
print(m1, end="\n\n")
print(m2, end="\n\n\n")

print("транспонирование матрицы")
m3.transpose()
print(m3)

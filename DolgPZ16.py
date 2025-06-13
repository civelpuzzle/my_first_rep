#Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
#Добавьте методы для сложения, вычитания и умножения матриц.
import random

user_input1 = int(input('Количество строк: '))
user_input2 = int(input('Количество столбцов: '))

class Matrix:
    """Класс Матрица"""
    def __init__(self, strok = user_input1, stolb = user_input2):
        self.strok = strok
        self.stolb = stolb

    def Create(self):
        self.matr = [[random.randint(-5, 5) for i in range(self.stolb)] for i in range(self.strok)]

    def Printtt(self):
        for i in self.matr:
            print(i)
        print('')
    def Add(self, other):
        self.sum = [[self.matr[i][y] + other.matr[i][y] for y in range(len(self.matr[0]))] for i in range(len(self.matr))]
        for i in self.sum:
            print(i)
        print(' ')
    def Sub(self, other):
        self.sub = [[self.matr[i][y] - other.matr[i][y] for y in range(len(self.matr[0]))] for i in range(len(self.matr))]
        for i in self.sub:
            print(i)
        print(' ')

    def Mult(self, other):
        self.mul = [[self.matr[i][y] * other.matr[i][y] for y in range(len(self.matr[0]))] for i in
                    range(len(self.matr))]
        for i in self.mul:
            print(i)
        print(' ')

matr = Matrix()
matr.Create()
matr.Printtt()

matr1 = Matrix()
matr1.Create()
matr1.Printtt()

matr1.Add(matr)
matr1.Sub(matr)
matr1.Mult(matr)
#Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m.
#Суммирование оформить функцией с параметрами. Значения n и m
#программа должна запрашивать

n = input("Введите начало ряда: ")
m = input("Введите конец ряда: ")

def proof(a): #обработка исключений
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            print("Неправильно ввели!")
            a = input("Введите число: ")
    return a 

def addis(a, b):
    summa = 0
    while a < b:
        summa += a
        a += 1
    print("Сумма ряда: ", summa)

n = proof(n)
m = proof(m)
addis(n, m)

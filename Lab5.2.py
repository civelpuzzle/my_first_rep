import random

K = input("Введите целое число: ")
D = 0

def proof(a):
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            print("Неправильно ввели!")
            a = input("Введите целое число: ")
    return a

K = proof(K)
#print(K)
#D = random.randint(0, 9)
#print(D)
#K = K * 10 + D
#print(K)
def AddRightDigit(a, b):
    a = random.randint(0, 9)
    b = b * 10 + a
    return b

K = AddRightDigit(D, K)
print(K)
K = AddRightDigit(D, K)
print(K)

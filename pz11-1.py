import random

f1 = open('data1.txt', 'w')

for i in range(10):
    f1.write(str(random.randint(-10, 10)) + ' ')

f1.close()

f1 = open('data1.txt')

first_data = f1.read()
first_data = first_data.split()
f1.close()

for i in range(len(first_data)):
    first_data[i] = int(first_data[i])

kolvo_el = len(first_data)

s1 = 0
plus_el = []
for i in range(len(first_data)):
    s1 += first_data[i]
    if first_data[i] > 0 and first_data[i] % 2 == 0:
        plus_el.append(first_data[i])
sr_znach1 = s1 / len(first_data)

sum_plus = 0
for i in range(len(plus_el)):
    sum_plus += plus_el[i]
sr_znach2 = sum_plus / len(plus_el)

f1 = open('data2.txt', 'w')
f1.write('Исходные данные: ')
f1.writelines(str(first_data))
f1.write('\nКоличество элементов: ')
f1.writelines(str(kolvo_el))
f1.write('\nСреднее арифметическое элементов: ')
f1.writelines(str(sr_znach1))
f1.write('\nПоложительные четные элементы: ')
f1.writelines(str(plus_el))
f1.write('\nСумма положительных четных элементов: ')
f1.writelines(str(sum_plus))
f1.write('\nСреднее арифметическое положительных четных элементов: ')
f1.writelines(str(sr_znach2))
f1.close()

f1 = open('data2.txt')
print(f1.read())
f1.close()

#Программа, находящая произведение всех целых чисел от A до B
#включительно

from tkinter import *

def proiz():
    try:
        n1 = int(num1.get())
        n2 = int(num2.get())
    except ValueError:
        result['text'] = ('Ошибка!')
        return
    sub = 0
    while n1 <= n2:
        sub += n1 * n2
        n1 += 1
    result['text'] = f"Результат: {sub}"

def laable(a):
    Label(text = "Ваше число").grid(row = a, column = 0)

def close():
    root.destroy()
    root.quit()

root = Tk()
root.title("PZ4-1")
root.geometry('300x120')

laable(1)
num1 = Entry()
num1.grid(row = 1, column = 1)

laable(2)
num2 = Entry()
num2.grid(row = 2, column = 1)

button = Button(text = 'Умножить', command = proiz)
button.grid(row = 3, column = 1)

result = Label()
result.grid(row = 4, column = 1)

root.protocol('WM_DELETE_WINDOW', close)

root.mainloop()

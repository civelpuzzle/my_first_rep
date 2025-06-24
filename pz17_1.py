from tkinter import *
from tkinter import ttk

def close():
    root.destroy()
    root.quit()

def laable(text_primer, row_primer):
    Label(text = text_primer).grid(row = row_primer, column = 0, sticky = "e", ipadx = 15)
    pole = Entry()
    pole.grid(row = row_primer, column = 1, columnspan = 3, ipadx = 40, pady = 5)

root = Tk()
root.title("Sign Up")
root.geometry('410x440')

laable("First Name", 1)
laable("Last Name", 2)
laable("Screen Name", 3)

#Date 0f Birth ОГРОМНЫЙ по коду
Label(text = "Date of Birth").grid(row = 4, column = 0, sticky = "e", ipadx = 15)
month = ["January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"]
combobox = ttk.Combobox(values=month, width = 9)
combobox.grid(row = 4, column = 1, columnspan = 1, pady = 5)
cifres = []
cifr = 1
for i in range(31):
    cifres.append(cifr)
    cifr += 1
combobox1 = ttk.Combobox(values=cifres, width = 4)
combobox1.grid(row = 4, column = 2, pady = 5)
god = 1985
goda = []
for i in range(41):
    goda.append(god)
    god += 1
combobox2 = ttk.Combobox(values=goda, width = 5)
combobox2.grid(row = 4, column = 3, pady = 5)

#GENDER
Label(text = "Gender").grid(row = 5, column = 0, sticky = "e", ipadx = 15)
var = IntVar()
rbutton1 = Radiobutton(root, text='Male', variable=var, value=1)
rbutton2 = Radiobutton(root, text='Female', variable=var, value=2)
rbutton1.grid(row = 5, column = 1, sticky = "w", pady = 5)
rbutton2.grid(row = 5, column = 2, sticky = "w", pady = 5)

#COUNTRY
Label(text = "Country").grid(row = 6, column = 0, sticky = "e", ipadx = 15)
country = ["USA", "RUSSIA", "JAPAN"]
combobox_coun = ttk.Combobox(values=country)
combobox_coun.grid(row = 6, column = 1, columnspan = 3, ipadx = 33, pady = 5)

laable("E-mail", 7)
laable("Phone", 8)
laable("Password", 9)
laable("Confirm Password", 10)

var1 = IntVar()
check = Checkbutton(root, text = 'I agree to the Terms of Use', variable = var1, offvalue = 0)
check.grid(row = 11, column = 1, columnspan = 2)

submitt = ttk.Button(root, text = "submit")
submitt.grid(row = 12, column = 1)
cancell = ttk.Button(root, text = "Cancel", command = close)
cancell.grid(row = 12, column = 2)

root.protocol('WM_DELETE_WINDOW', close)

root.mainloop()

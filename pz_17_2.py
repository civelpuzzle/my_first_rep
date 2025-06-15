import tkinter as tk
from tkinter import ttk

def submit_form():
    # Здесь можно добавить логику обработки данных формы
    print("Форма отправлена")

root = tk.Tk()
root.title("Sign Up")

# Основной фрейм для содержимого
main_frame = ttk.Frame(root, padding="20")
main_frame.pack()

# Заголовок
ttk.Label(main_frame, text="Sign Up", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

# Поля формы
fields = [
    ("First Name", "Enter First Name..."),
    ("Last Name", "Enter Last Name..."),
    ("Screen Name", "Enter Screen Name..."),
    ("E-mail", "Enter E-mail......"),
    ("Phone", "Enter Phone......"),
    ("Password", ""),
    ("Confirm Password", "")
]

for i, (label_text, placeholder) in enumerate(fields, start=1):
    ttk.Label(main_frame, text=label_text).grid(row=i, column=0, sticky="w", pady=2)
    entry = ttk.Entry(main_frame)
    entry.grid(row=i, column=1, pady=2, sticky="ew")
    if placeholder:
        entry.insert(0, placeholder)

# Дата рождения
ttk.Label(main_frame, text="Date of Birth").grid(row=8, column=0, sticky="w", pady=2)
birth_frame = ttk.Frame(main_frame)
birth_frame.grid(row=8, column=1, sticky="w")

month_var = tk.StringVar(value="May")
day_var = tk.StringVar(value="5")
year_var = tk.StringVar(value="1985")

ttk.Combobox(birth_frame, textvariable=month_var, values=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], width=5).pack(side="left")
ttk.Entry(birth_frame, textvariable=day_var, width=3).pack(side="left", padx=5)
ttk.Entry(birth_frame, textvariable=year_var, width=5).pack(side="left")

# Пол
ttk.Label(main_frame, text="Gender").grid(row=9, column=0, sticky="w", pady=2)
gender_frame = ttk.Frame(main_frame)
gender_frame.grid(row=9, column=1, sticky="w")

gender_var = tk.StringVar()
ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left")
ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left", padx=10)

# Страна
ttk.Label(main_frame, text="Country").grid(row=10, column=0, sticky="w", pady=2)
country_var = tk.StringVar(value="USA")
ttk.Combobox(main_frame, textvariable=country_var, values=["USA", "Canada", "UK", "Australia", "Other"]).grid(row=10, column=1, sticky="ew")

# Соглашение
agree_var = tk.IntVar()
ttk.Checkbutton(main_frame, text="I agree to the Terms of Use", variable=agree_var).grid(row=11, column=0, columnspan=2, pady=10)

# Кнопки
buttons_frame = ttk.Frame(main_frame)
buttons_frame.grid(row=12, column=0, columnspan=2, pady=10)

ttk.Button(buttons_frame, text="Submit", command=submit_form).pack(side="left", padx=5)
ttk.Button(buttons_frame, text="Cancel", command=root.destroy).pack(side="left")

# Настройка отступов и растягивания
for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=2)

root.mainloop()
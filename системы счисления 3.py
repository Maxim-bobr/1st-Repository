import tkinter as tk
from tkinter import ttk

def show_input_originalnum():
   # получаем данные из поля
   user_input_originalnum = original_number.get()


# Создаю окно
root = tk.Tk()

root.title("Перевод из одной системы счисления в другую")

root.geometry("1000x200")
# Строка приветствия
label = tk.Label(root, text="Привет! Тут ты сможешь перевести число из одной системы счисления в другую", font=("Arial",14))
label.grid(column=1, row=0, sticky="w", padx=5)

# Строка для исходного числа
label = tk.Label(root, text="Введи число, которое хочешь перевести в другую систему счисления", font=("Arial",14))
label.grid(column=1, row=1, sticky="w", ipadx=5)

# Создаю поле ввода числа для перевода в другую систему счисления
original_number = tk.Entry(root, font=("Arial", 14))
# задаём отступы сверху и снизу
original_number.grid(column=1, row=3, sticky="w", padx=10)

# Создаём выбор между системами счисления
combo_of_values = ttk.Combobox(root, values=["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"])
combo_of_values.grid(column=1, row=3, sticky="w", padx=250)

# Знак равно
label = tk.Label(root, text="=", font=("Arial",25))
label.grid(column=1, row=3, sticky="w", padx=410)

# Вывод обработанного результата
final_value = tk.Text(root, height=1, width=20, font=("Arial", 14))
final_value.grid(column=1, row=3, sticky="w", padx=450)

combo_of_values_2 = ttk.Combobox(root, values=["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"])
combo_of_values_2.grid(column=1, row=3, sticky="w", padx=250)

root.mainloop()


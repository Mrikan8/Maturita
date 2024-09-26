import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.withdraw()

a = int(input('zadej a: '))
b = int(input('zadej b: '))

if b != 0:
    podil = a // b
    messagebox.showinfo("Výsledek", f'podil: {podil}')
else:
    messagebox.showerror("Chyba", 'nulou se nedělí ani v něděli')
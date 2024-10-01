import math
import tkinter as tk
from tkinter import messagebox

def rovnostranny_trojuhelnik(s):
    o = 3 * s
    s = (math.sqrt(3) / 4) * (s ** 2)
    return o, s

def vypocet():
    try:
        s = float(entry.get())
        o, obsah = rovnostranny_trojuhelnik(s)
        messagebox.showinfo("Výsledek", f"Obvod: {o:.1f}\nObsah: {obsah:.1f}")
    except ValueError:
        messagebox.showerror("Chyba", "Prosím zadejte platné číslo.")

root = tk.Tk()
root.title("Rovnostranný trojúhelník")

tk.Label(root, text="Zadejte délku strany rovnostranného trojúhelníku:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Vypočítat", command=vypocet).pack(pady=20)

root.mainloop()
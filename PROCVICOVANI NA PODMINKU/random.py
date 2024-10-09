import os
import math
import random

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu(vyber=None):
    clear_terminal()
    vyber = input('Vyber jakou operaci chceš udělat: \n1. Kalkulačka \n2. Password cracker \n3. todo list \n')
    if vyber == '1':
        kalkulacka()
    elif vyber == '2':
        password_cracker()
    elif vyber == '3':
        todo_list()
    else:
        print('Neplatná volba.')
        return menu(vyber)

def scitani():
    clear_terminal()
    print('Sčítání')
    a = float(input('Zadej první číslo: '))
    b = float(input('Zadej druhé číslo: '))
    print(f'Výsledek: {a + b}')
def odcitani():
    clear_terminal()
    print('Odčítání')
    a = float(input('Zadej první číslo: '))
    b = float(input('Zadej druhé číslo: '))
    print(f'Výsledek: {a - b}')

def kalkulacka():
    clear_terminal()
    print('Kalkulačka')
    pocitat = input ('Chceš sčítat nebo odčítat? \n1. Sčítat \n2. Odčítat \n')
    if pocitat == '1':
        scitani()
    elif pocitat == '2':
        odcitani()
    else:
        print('Neplatná volba.')
        return kalkulacka()

def password_cracker():
    clear_terminal()
    print('Password cracker')
    crack = input('Zadej počet pokusů:')
    random_number = random.randint(0, 100)
    print(f'Password: {random_number}')






def todo_list():
    clear_terminal()
    print('Todo list')

menu()
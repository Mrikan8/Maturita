a = int(input('Zadej a: '))
b = int(input('Zadej b: '))

if b == 0:
    print("Nulou se nedělí ani v neděli.")
    exit()
original_a = a 

while a >= b:
    print('prdním!')
    a -= b

print(f"Zbytek po dělení {original_a} číslem {b} je {a}")
n = int(input('Zadej číslo n: '))
c = int(input('Zadej číslici, kterou chceš v n vyhledat: '))

n_str = str(n)
c_str = str(c)

if c_str in n_str:
    print(f"Číslice {c} se v čísle {n} vyskytuje.")
else:
    print(f"Číslice {c} se v čísle {n} nevyskytuje.")

p = n_str.count(c_str)
print(f"Počet výskytů číslice {c} v čísle {n} je {p}.")
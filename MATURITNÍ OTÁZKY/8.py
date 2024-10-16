# sestavte algoritmus pro cýpočet součtu přirozených čísel větších rovno N1 a menších nebo rovno N2

N1 = int(input('Zadej číslo N1: '))
N2 = int(input('Zadej číslo N2: '))
i = N1
soucet = 0

while i <= N2:
    soucet = soucet + i
    i = i + 1
print(i, soucet)
# sestavte algoritmus pro výpočet průměrné známky z n známek

n = int(input('Zadej počet známek: '))
soucet = 0

for i in range(n):
    znamka = float(input(f'Zadej známku {i + 1}: '))
    soucet += znamka

prumer = soucet / n
print(f'Průměrná známka je: {prumer}')


import math

a = float(input('Zadej a: '))
b = float(input('Zadej b: '))
c = float(input('Zadej c: '))

D = b**2 - 4*a*c

if D >= 0:
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f'Kořen x1 je {x1}')
        print(f'Kořen x2 je {x2}')
    else:
        x = -b / (2*a)
        print(f'Kořen x je {x}')
else:
    print('Rovnice nemá řešení')

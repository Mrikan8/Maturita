a = float(input('zadej a: '))
b = float(input('zadej b: '))

if a != 0:
    x = -b / a
    print(f'x = {x}')
if b != 0:
    print('Rovnice nemá řešení')
else:
    print('Rovnice má nekonečně mnoho řešení')
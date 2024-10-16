heslo_zadane = 'ahoj'

for pokus in range(3):
    heslo = input('Zadej heslo: ')
    if heslo == heslo_zadane:
        print('Správně!')
        input()
        break
    else:
        print(f'Špatně!, zbývají ještě {2 - pokus} pokusy')
else:
    print('Máš blok')
    input()
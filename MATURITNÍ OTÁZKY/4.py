heslo = 'ahoj'
max_pokusy = 3
pokusy = 0


while pokusy < max_pokusy:
    pokus = input('Zadej heslo: ')
    if pokus == heslo:
        print('Správně')
        input()
        break
    else:
        pokusy += 1
        if pokusy < max_pokusy:
            print(f'Zkus to znovu, máš ještě {max_pokusy - pokusy} pokusů')
if pokusy == max_pokusy:
    print('Konec, zadal si špatné heslo 3x za sebou')
    input()

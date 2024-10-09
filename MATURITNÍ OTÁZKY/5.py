while True:
    heslo = int(input('Zadej heslo: '))
    if heslo == 1234:
        print('Správné heslo')
        break
    else:
        print('Špatné heslo, zkuste to znovu.')
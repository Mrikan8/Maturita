cislo1 = int(input("Zadejte první číslo: "))
cislo2 = int(input("Zadejte druhé číslo: "))

if cislo1 > cislo2:
    print(f"Větší číslo je: {cislo1}")
elif cislo1 < cislo2:
    print(f"Větší číslo je: {cislo2}")
else:
    print("Obě čísla jsou stejná.")

a = float((input("Zadejte a: ")))
b = float((input("Zadejte b: ")))
max = b

if a > b:
    a = max
    print("Větší číslo je", max)
    
else:
    if a == max:
        print("Čísla jsou stejná")
    else:
        print("Větší číslo je", max)

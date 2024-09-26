a = float((input("Zadejte a: ")))
b = float((input("Zadejte b: ")))
max = b
if a > max:
    max = a
    print("Větší číslo je", max)

elif a == b:
    print("Čísla jsou stejná")
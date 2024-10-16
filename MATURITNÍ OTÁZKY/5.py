a = int(input("Zadejte první číslo: "))
b = int(input("Zadejte druhé číslo: "))
c = int(input("Zadejte třetí číslo: "))

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(c, b, a)
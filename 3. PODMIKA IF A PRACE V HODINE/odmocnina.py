import math
import cmath

a = float(input('zadej a: '))
if a < 0:
    a = cmath.sqrt(a)
    a_str = str(a).replace('j', 'i')
    print(a)
else:
    a = math.sqrt(a)
    print(a)
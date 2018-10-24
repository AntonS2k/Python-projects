import math
x = float(input('Введите число '))
if x >= -math.pi and x <= math.pi:
    print(math.cos(3*x))
else:
    print(x)

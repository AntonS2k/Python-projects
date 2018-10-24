import math
print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = float(input('число a = '))
b = float(input('число b = '))
c = float(input('число c = '))
discr = b**2 - 4 * a * c # Дискриминант D = b^2 - 4ac
print("Дискриминант D = ", discr)
if discr > 0: # Если D > 0, то квадратное уравнение имеет два корня x1 = (-b + корень b^2 - 4ac)/2a  и  x2 = (-b - корень b^2 - 4ac)/2a
	x1 = (-b + math.sqrt(discr)) / (2 * a)
	x2 = (-b - math.sqrt(discr)) / (2 * a)
	print("Корень х1 = ", x1, "Корень х2 = ", x2)
elif discr == 0: #если D = 0, то 1 корень x1=x2=-b/2a
	x = -b / (2 * a)
	print(x)
else: #если D < 0, то делают вывод, что корней нет.
	print("Корней нет")
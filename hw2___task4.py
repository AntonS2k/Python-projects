a = float(input('Введите число 1 '))
b = float(input('Введите число 2 '))
if a > b:
    print(a/b)
elif b>a:
    print (a+b)
elif a==b:
    print('каждое число равно', a)
else:
    print('отсутствует условие')

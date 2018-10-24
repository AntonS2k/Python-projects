a = int(input('Введите год '))
if a%400==0:
    print('високосный')
elif a%100==0:
    print('високосный')
elif a%4==0:
    print('високосный')
else:
    print('невисокосный')


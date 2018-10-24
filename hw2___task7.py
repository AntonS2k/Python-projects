a = int(input('Введите год '))
if a%4==0 and a%100==0 and a%400:
    print('високосный')
else:
    print('невисокосный')


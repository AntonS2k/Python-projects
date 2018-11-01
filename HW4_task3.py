# Создайте программу-калькулятор, которая поддерживает четыре операции: сложение, вычитание, умножение, деление.
# Все данные должны вводиться в цикле, пока пользователь не укажет, что хочет завершить выполнение программы.
# Каждая операция должна быть реализована в виде отдельной функции.
# Функция деления должна проверять данные на корректность и выдавать сообщение об ошибке в случае попытки деления на ноль.


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

flag = True
res = None
while flag:
    x = int(input('please type integer 1 '))
    y = int(input('please type integer 2 '))
    operation = (input('operation is '))

    if y == 0 and operation == '/':
        print('невверный ввод')
    elif operation == '*':
        res = mul(x, y)
    elif operation == '/':
        res = div(x, y)
    elif operation == '+':
        res = add(x, y)
    elif operation == '-':
        res = sub(x, y)
    stop = input('Введите stop, чтобы остановить цикл : ')
    if stop == 'stop':
        flag = False

    if res:
        print(res)

print(res)

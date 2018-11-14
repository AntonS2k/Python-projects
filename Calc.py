def add(a , b):
    return a + b

def sub(a , b):
    return a - b

def mul (a, b):
    return a*b

def div (a, b):
    loop = True
    while loop:
        try:
            print('Result:', a / b)
            loop = True
        except (ValueError, ZeroDivisionError) as error:
            print('Error:', error)
            print('Please try again')
            print()
            loop = False



import math as m

MATH_OPERATION = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    'log': m.log,
}

def main():
    while True:
        try:
            x = float(input('>> '))
            y = float(input('>> '))
            oper  = input('Operation is: ')
            res = MATH_OPERATION[oper](x , y)
            if res:
                print('Result:',res)
            elif res == 0:
                    print ('Result: 0')
        except ValueError:
            print("Please type valid data")
main()
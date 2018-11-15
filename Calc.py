def add(a , b):
    return a + b

def sub(a , b):
    return a - b

def mul (a, b):
    return a*b

def div (a, b):
    while True:
        try:
            print('Result:', a / b)
            break
        except (ValueError, ZeroDivisionError) as error:
            print('Error:', error)
            print('Please try again')
            break

def cos (a):
    return math.cos(a)

import math as m

TRIG_OPERATION = {
    'cos': m.cos,
    'sin': m.sin,
    }

MATH_OPERATION = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    'log': m.log,
    '**': pow,
    }


def main():
    while True:
        try:
            x = float(input('>> '))
            y = float(input('>> '))
            oper = input('Operation is: ')
            res = MATH_OPERATION[oper](x , y)
            x = float(input('>> '))
            trig_func = input('trigonometric function is: ')
            res_trig = TRIG_OPERATION[trig_func](x)
            if res and res_trig:
                print('Result:',res)
                print('Result:', res_trig)
            elif res == 0 and res_trig==0 :
                print ('Result: 0')
        except (ValueError, KeyError) as error:
            print("Please type valid data")

main()

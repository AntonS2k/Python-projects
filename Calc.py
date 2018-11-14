# def cos (a):
#     return math.cos(a)

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

import math as m

MATH_OPERATION = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    'log': m.log,
    '**': pow,
    # 'cos': m.cos,
    }

def main():
    while True:
        try:
            x = float(input('>> '))
            y = float(input('>> '))
            oper  = input('Operation is: ')
            res = MATH_OPERATION[oper](x , y) or MATH_OPERATION[oper](x)
            if res:
                print('Result:',res)
            elif res == 0:
                print ('Result: 0')
            # elif oper == 'cos':
            #     print('Cosine:', m.cos(x))
        except (ValueError, KeyError) as error:
            print("Please type valid data")
main()
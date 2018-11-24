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

TRIG_OPERATION = {
    'cos': m.cos,
    'sin': m.sin,
    'tan': m.tan,
    }

MATH_OPERATION = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    'log': m.log,
    '**': pow,
    }


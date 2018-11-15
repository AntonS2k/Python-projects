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

def main():
    try:
        x = float(input('>> '))
    except (ValueError, KeyError, UnboundLocalError) as error:
        print("Please type valid data")
    oper = input('Operation is: ')
    if oper == '+' or oper == '-' or oper == '*' or oper == '/' or oper == 'log' or oper == '**':
            try:
                y = float(input('>> '))
                res = MATH_OPERATION[oper](x , y)
                if res:
                    print('Result:',res)
                elif res == 0:
                    print ('Result: 0')
            except (ValueError, KeyError) as error:
                print("Please type valid data")

    else:
            try:
                res_trig = TRIG_OPERATION[oper](x)
                if res_trig:
                    print('Result:', res_trig)
                elif res_trig == 0 :
                        print ('Result: 0')
            except (ValueError, KeyError, UnboundLocalError) as error:
                print("Please type valid data")
main()
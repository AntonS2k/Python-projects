from Calc_def import TRIG_OPERATION
from Calc_def import MATH_OPERATION
import math as m

def main():
    try:
        x = float(input('>> '))
    except (ValueError, KeyError, UnboundLocalError) as error:
        print('Please type valid data')
    oper = input('Operation is: ')
    if oper in MATH_OPERATION.keys():
            try:
                y = float(input('>> '))
                res = MATH_OPERATION[oper](x , y)
                if res is not None:
                    print('Result:',res)
            except (ValueError, KeyError) as error:
                print('Please type valid data')

    elif oper in TRIG_OPERATION.keys():
            try:
                res_trig = TRIG_OPERATION[oper](x)
                if res_trig is not None:
                    print('Result:', res_trig)
            except (ValueError, KeyError, UnboundLocalError) as error:
                print('Please type valid data')
    else:
        print ('Please type valid operator')
main()
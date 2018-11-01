# Создайте две функции, вычисляющие значения определённых алгебраических выражений.
# Выведите на экран таблицу значений этих функций от -5 до 5 с шагом 0.5.


def functionadd():
    step = 0.5
    for i in range(-5, 5):
        i += step
        print('all added digits', i)
functionadd()

print ('_________________________')

def functionsub():
    step = 0.5
    for i in range(-4, 5):
        i -= step
        print('all subtracted  digits', i)
functionsub()
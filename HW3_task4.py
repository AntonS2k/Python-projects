width  = int(input("Введите ширину прямоугольника :"))
height  = int(input("Введите высоту прямоугольника :"))

for zvezda_visota in range(height):
    for zvezda_shirina in range(width):
        print('*', end='')
    print()
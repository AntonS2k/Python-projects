n = int(input('введите число '))
for a in range(0, n):
    for b in range (0, n-a-1):
        print(end='')
    for b in range(0, a+1):
        print('*', end='')
    print()
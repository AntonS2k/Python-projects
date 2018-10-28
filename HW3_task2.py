num = int(input('Enter factorial n: '))
if num < 0:
    print("error - negative number")
elif num == 0:
        print("The factorial of 0 is 1")
else:
    for i in range(1, num, +1):
        factorial = num * i
print("The factorial of",num,"is",factorial)
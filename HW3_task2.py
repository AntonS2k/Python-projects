n = int(input('Enter factorial n: '))
f=1
if n < 0:
    print("error - negative number")
elif n == 0:
        print("The factorial of 0 is 1")
else:
    for i in range(1, n+1):
        f *= i
print("The factorial of",n,"is",f)

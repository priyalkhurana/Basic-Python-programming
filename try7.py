a=["0","2","3"]
try:
    print(a[3])
except IndexError:
    print("Can't be executed..Index error")
try:
    b=int(input("Enter number for division"))
    print(b/ int(a[0]))
except ArithmeticError:
    print("Division by zero is not possible")
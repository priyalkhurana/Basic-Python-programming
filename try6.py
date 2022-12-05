try:
    marks=int(input("Enter marks"))
    if(marks<35):
        raise ValueError
    else:
        print("PASS!")
except ValueError:
    print("FAILED")
    
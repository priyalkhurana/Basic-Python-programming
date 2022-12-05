n=int(input())
for i in range(n):
    try:
        a=int(input())
        b=int(input())
        d=(a//b)
        print(d)
    except ZeroDivisionError as f1:
        print("Error Code",f1)
    except ValueError as f2:
        print("Error Code",f2)
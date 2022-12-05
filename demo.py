n=int(input("enter the total no. of stamps : "))
stamp=set(input("enter the name of country the stamp belong to : "))
for i in range(0,n):
    stamp.add(input()) 
print("total no. of distinct country stamps:",len(stamp)) 
print("rupal has stamps of countries: ",stamp)

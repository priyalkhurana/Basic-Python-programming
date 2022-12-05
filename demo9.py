list1=[4,2,8,"4",5,6]
sum=0
for i in list1:
    try:
        sum=sum+i
    except TypeError:
        print("Can't add string To an integer")
    print("SUM=",sum)
    try:
        print(list[6])
    except IndexError:
        print("Index Out of Range")
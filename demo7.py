with open("city.txt","r+") as f1:
    data=f1.read()
    print(data)
print()
with open("city.txt","r+") as f2:
    print("Cities with population more than 10 lakhs::")
    lines=f2.readlines()
    for line in lines:
        w=line.split()
        word=list(w)
        if(float(word[1])>10):
            print(word[0])
    print()
    print("sum of areas of all cities:")
    sum=0.0
    for line in lines: 
        w=line.split()
        wo=list(w)
        sum=sum+float(w[2])
    print(sum)
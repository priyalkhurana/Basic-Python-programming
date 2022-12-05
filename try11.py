count=0
with open("file1.txt","r") as f1:
    a=f1.readlines()
    for a in f1:
        x=a.split(' ')
        if(x=='Hello'):
            count=count+1
print(count)
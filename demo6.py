with open("city.txt",'r+') as f:
    data=f.read()
    print(data)
print()
with open("city.txt",'r+') as f:
    print("Cities with population more than 10lakhs::")
    lines= f.readlines()
for line in lines
count=0
str=input("Enter a string: ")
substr=input("Enter a substring: ")
for i in range(len(str)):
    if(str[i:i+len(substr)]==substr):
        count=count+1
print(count)
print(type(i))
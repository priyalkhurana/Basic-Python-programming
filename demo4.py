with open("file1.txt",'r+') as f1:
    data=f1.read()
    print(data)
print()
with open("file2.txt",'a') as f2:
    f2.write(data.replace('\"','\\"'))
with open("file2.txt",'r+') as f2:
    print(f2.read())
f1.close()
f2.close()
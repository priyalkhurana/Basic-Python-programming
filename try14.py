#copy contents of one file to another
f1=open("file1.txt","r")
f2=open("file1new.txt","w")
for x in f1:
    f2.write(x.replace("Hello","HEY"))
f2=open("file1new.txt","r")
print(f2.read())
f1.close()
f2.close()
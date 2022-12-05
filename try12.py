#to read number of words in a file
f=open("file1.txt","r")
x=f.read()
numw=x.split()
print("number of words",len(numw))
#number of occ. of a word
file1=open("file1.txt","r")
data=file1.read()
num=data.count("Hello")
print("number of occ.",num)
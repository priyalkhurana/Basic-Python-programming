a= ["Hello!\n", "How\n", "are\n","you\n","?\n"]
 
with open("myfile.txt", "w") as f1:
    f1.writelines(a)

#def longestLength(a):
max1 = len(a[0])
temp = a[0]
  
# for loop to traverse the list
for i in a:
     if(len(i) > max1):
  
        max1 = len(i)
        temp = i
  
print("The word with the longest length is:", temp)
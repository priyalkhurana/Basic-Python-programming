L = ["Hello!\n","Good morning!\n", "How\n", "are\n","you\n","?\n"]
 
with open("myfile.txt", "w") as f1:
    f1.writelines(L)
i= 0
with open("myfile.txt") as f1:
    Lines = f1.readlines()
    for line in Lines:
        i += 1
print("Number of lines in file=",i)
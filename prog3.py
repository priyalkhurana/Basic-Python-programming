L = ["Hello!", "How", "are","you","?"]
 
with open("myfile.txt", "w") as f1:
    f1.writelines(L)
i= 0
with open("myfile.txt") as f1:
    Lines = f1.readlines()
    for line in Lines:
        print(line)
f1 = open('myfile.txt', 'a')
# Append 'hello' at the end of file
f1.write('Welcome to the coding world!')
# Close the file
with open("myfile.txt") as f1:
    Lines = f1.readlines()
    for line in Lines:
        print(line)

f1.close()
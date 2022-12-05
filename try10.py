L=['Priyal\n','18years\n','First year\n','April\n','2021']
with open("myfile.txt", "w") as f1:
    f1.writelines(L)

with open("myfile.txt") as f1:
    Lines = f1.readlines()
    print(Lines)
try:
    with open("file1.txt","r+") as f1:
        data=f1.read()
        print(data)
    print()
    with open("file2.txt",'a') as f2:
        try:
            f2.write(data.replace('\"','\\"'))
            raise ValueError
        except ValueError:
            print("Data to be replaced not found")
    with open ("file3.txt",'r+') as f2:
            print(f2.read())
except FileNotFoundError:
    print("NO SUCH FILE EXIST!")


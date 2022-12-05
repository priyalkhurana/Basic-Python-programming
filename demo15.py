from tkinter import *
def username():
    pname = uia.get()
    print("User name is",pname)
    
def click_me():
    print("Button was clicked") 

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text = selection)
    print(selection)

root = Tk()
root.geometry('500x500')
root.title("First program")
l=Label(root,text="Hello").pack()
user_name=Label(root,text="Username").place(x=100,y=100)
uia=Entry(root)
uia.pack(padx=100,pady=80)

but = Button(root, text='Click me',bg = "black",fg ="green",width=10,command=click_me).place(x=200,y=300)
bu = Button(root, text='stop',border=3,width=10,command=root.destroy).place(x=200,y=350)
button = Button(root, text='Submit UserName',command=username).place(x=200,y=130)

var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                  command=sel)
R1.pack()

R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
                  command=sel)
R2.pack()

R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                  command=sel)
R3.pack()

label = Label(root)
label.pack()
root.mainloop()

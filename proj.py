from tkinter import *




def staff():

    def submitt():   
        pname = uia.get()
        m1=ma.get()
        m2=mar.get()
        m3=marks.get()
        avg=(int(m1)+int(m2)+int(m3))
        labe=Label(window,text="Patient's name "+pname,font = "Arial").place(x=500,y=750)
        lab=Label(window,text ="The Total amount is "+ str(avg) ,font = "Arial").place(x=500,y=750)

    window = Tk()
    window.geometry('800x800')
    window.title("Patient details")

    l=Label(window,text="Fill up the following details",font = "Arial").place(x=300,y=10)

    user_name=Label(window,text="Patient's Name",font = "Arial").place(x=200,y=55)
    uia=Entry(window)
    uia.place(x=300,y=60)



    sub=Label(window,text="Select the Gender",font = "Arial").place(x=210,y=240)
    var = StringVar()
    R1 = Radiobutton(window, text="Male", variable=var, value="Male",font = "Arial")
    R1.place(x=300,y=100)
    R2 = Radiobutton(window, text="Female", variable=var, value="Female",font = "Arial")
    R2.place(x=300,y=140)
    R3 = Radiobutton(window, text="Marks", variable=var, value="Marks",font = "Arial")
    R3.place(x=300,y=180)



    sub=Label(window,text="Select the Consulted Doctor"
              ,font = "Arial").place(x=80,y=260)
    listbox = Listbox(window, height = 4,width = 20,font = "Helvetica")
    listbox.insert(1, "Dr. Priyal Khurana")
    listbox.insert(2, "Dr. Kanishka Kathait")
    listbox.insert(3, "Dr. Mitali Chaudhary")
    listbox.insert(4, "Dr. Vrinda Kumar")
    listbox.place(x=300,y=230)


    sub=Label(window,text="Enter fee of three subject",font = "Arial").place(x=200,y=350)
    l1=Label(window,text="consultation Fee").place(x=340,y=490)
    l2=Label(window,text="Medication fee").place(x=340,y=530)
    l3=Label(window,text="Medical reports'fee").place(x=340,y=570)
    ma=Entry(window)
    ma.place(x=400,y=490)
    mar=Entry(window)
    mar.place(x=400,y=530)
    marks=Entry(window)
    marks.place(x=400,y=570)
    button = Button(window, text='Submit details', bd=10,width=25,bg = "black",fg ="teal",command=submitt).place(x=400,y=700)

    window.mainloop()


try:
    ch=int(input("Enter Designation : 1. Staff \n 2. Doctor \n 3. Patient \n"))
    #print("1.")
    if(ch==1):
        staff()
    #if(ch==2):
        #doctor()
    else:
        print("TRY AGAIN")
except ValueError:
    print("LOGIN FAILED!!")

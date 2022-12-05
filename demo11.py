class Employee:
    def __init__(self, fname, lname, pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay

    def func(self):
        print("Information of an Employee::")
        print("First name=",self.fname)
        print("Last name=",self.lname) 
        print("Pay=",self.pay)
        print("Email=",self.fname+'.'+self.lname+"@upes.ac.in")
a1= Employee("Mohandas","Gandhi", 500000)
a1.func()
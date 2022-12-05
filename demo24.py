class student:
    def details(self):
        self.name=input("Enter student name \t")
        self.roll=input("Enter roll no. \t") 
        self.crse=input("Enter applied course \t")
class course(student): 
    def display(self):
        print(self.name+" having roll number",self.roll,"is being enrolled in",self.crse +" sucessfully")
c1=course() 
c1.details()
c1.display()

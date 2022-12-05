#Write a program to accept student info in a student class
#  and register a student for a course using course class. 
#Use inheritance
class student:
    course="not applicable"
    def __init__(self,name,age):
        self.name=name
        self.age=age
class coursec(student):
    def __init__(self,name,age,percent):
        student.__init__(self,name,age)
        self.percent=percent
        if(self.percent>=90):
            self.course="Science"
        elif(self.percent>=70 and self.percent<90):
            self.course="Commerce"
        else:
            self.course="Humanities"
    def display(self):
        print("\nname=",self.name)
        print("\nage=",self.age)
        print("\nCourse=",self.course)

a1=coursec("Priyal",18,93)
a1.display()
a2=coursec("Ankita",18,70)
a2.display()
a3=coursec("Rahul",18,45)
a3.display()
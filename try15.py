#create a class and write the function to receive name and age of a user and display the values by writing another function
class sample:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name=",self.name)
        print("\nage=",self.age)

a1=sample("Priyal",18)
a1.display()
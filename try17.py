#write a program to create a class vehicle and 
# make a function for accepting seating capacity and model of the vehicle 
# and create a child class to print whether the speed of the car is safe or not.
#Criteria for judging the speed is speed limit between 60 -90.

class vehicle:
    def __init__(self,seating_cap,model):
        self.seating_cap=seating_cap
        self.model=model
    def result(self):
         print(self.seating_cap,self.model)
class display(vehicle):
    speed=0
    def limit(self,speed):
        if((speed>=60) and (speed<=90)):
            print("\n   SAFE!!")
        else:
            print("NOT SAFE!!")
c1=display(4,"2019FORD")
c1.result()
c1.limit(70)

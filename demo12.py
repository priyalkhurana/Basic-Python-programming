class vehicle:
    def __init__ (self,name,max_speed, mileage):
        self.name= name 
        self.max_speed=max_speed
        self.mileage=mileage
    def attribute(self):
        print("\n Vehicle attributes are::")
        print("Model name :",self.name)
        print("\nTop speed :",self.max_speed)
        print("\n Mileage :",self.mileage)
    def seating_cap(self,capacity):
        print("\n Seating capacity :")
        return(f"The seating capacity of {self.name} is {capacity} passengers")
class Bus(vehicle):
    print("Please provide Vehicle information\n")
    name=input("Enter name of Vehicle :")
    max_speed=int(input("\n Top speed"+ name +" offer :"))
    mileage= int(input("\nMileage"+name+" offer"))
    capacity=int(input("\n Enter the capacity of "+ name+" offer :"))
    bus=vehicle(name,max_speed,mileage)
    vehicle.attribute(bus)
    seats=vehicle.seating_cap(bus,capacity)
    print (seats)
class colour:
    def __init__(self, vehicle_colour="black"):
        self.vehicle_colour=vehicle_colour
    def colours(self):
        print(f"\n Colour of every vehicle is {self.vehicle_colour}")
class colours(colour):
    vehicle_colour= colour()
    colour.colours(vehicle_colour)

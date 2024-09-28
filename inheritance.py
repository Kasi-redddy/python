class Vehicle:  # Corrected class name
    def general_usage(self):
        print("General use: Transportation")

class Car(Vehicle):  # Corrected class name
    def __init__(self):
        self.wheels = 4
        self.has_roof = True
        
    def specific_usage(self):
        print("Specific use: Commute to vacation with family")

class MotorCycle(Vehicle):  # Corrected class name
    def __init__(self):
        print("I am a bike")
        self.wheels = 2
        self.has_roof = False
        
    def specific_usage(self):
        print("Specific use: Commute and racing")

# Creating an object of Car and calling methods
c = Car()
c.general_usage()
c.specific_usage()

# Creating an object of MotorCycle and calling methods
m = MotorCycle()
m.general_usage()
m.specific_usage()

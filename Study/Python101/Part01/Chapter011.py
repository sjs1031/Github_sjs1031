x = "Mike"
#print(dir(x))

# Creating a Class
class Vehicle:
    """docstring"""

    def __init__(self):
        """Constructor"""
        pass

print("")

class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires

    def brake(self):
        """
        Stop the Car
        """
        return "Braking"
    
    def drive(self):
        """
        Drive the Car
        """
        return "I'm Driving"

# What is self?
if __name__ == "__main__":
    car = Vehicle("blue",5,4)
    print(car.color)

    truck = Vehicle("red",3,6)
    print(truck.color)

print("")

class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype
    
    def brake(self):
        """
        Stop the Car
        """
        return "%s Braking" % self.vtype
    
    def drive(self):
        """
        Drive the Car
        """
        return "I'm Driving a %s %s!" % (self.color, self.vtype)
'''
if __name__ == "__main__":
    car = Vehicle("blue",5,4,"Car")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("red", 3, 6, "truck")
    print(truck.drive())
    print(truck.brake())
'''
print("")

# Subclasses
class Car(Vehicle):
    """
    The Car class
    """
    #----------------------------------------------------------------
    def brake(self):
        """
        Override brake method
        """
        return "The car class is breaking slowly!"

if __name__ == "__main__":
    car = Car("yellow", 2, 4, "car")
    car.brake()
    car.drive()

    

#vehicle system using  abstraction
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def brake(self): #concrete method
        print("Vehicle is braking")
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")    
car=Car()
#obj=Vehicle
bike=Bike() 
car.start_engine()
bike.start_engine()
car.brake()
bike.brake()
#obj.start_engine() #error because we cannot create object of abstract class and also we cannot call abstract method using class name because it is not implemented in abstract class but implemented in child class only then we can call using child class object like
#obj.brake() #error because we cannot call concrete method using class name because it is not implemented in abstract class but implemented in child class only then we can call using child class object like
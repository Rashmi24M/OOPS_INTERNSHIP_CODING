#vehicle system using  abstraction
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def brake(self):
        print("Vehicle is braking")
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")    
car=Car()
bike=Bike() 
car.start_engine()
bike.start_engine()
car.brake()
bike.brake()
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sleep(self):
        print("Animal is sleeping")
class Dog(Animal):
    def sound(self):
        print("barks")
class Cat(Animal):
    def sound(self):
        print("meows")
class Cow(Animal):
    def sound(self):
        print("moo")
dog=Dog()
cat=Cat()   
cow=Cow()   
dog.sound()
cat.sound()         
cow.sound()
dog.sleep()
cat.sleep()
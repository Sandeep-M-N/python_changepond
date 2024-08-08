from abc import ABC, abstractmethod

#define an abstract base class
class Animal:
    @abstractmethod
    def sound(self):
        pass

#define a conrete class that inherites from the abstract base class
class Dog(Animal):
    def sound(self):
        return "barks"
    
# define a another  concrete class
class Cat(Animal):
    def sound(self):
        return "Meow"
    
#Instantiating and using concrete subclasses
d1=Dog()
c1=Cat()
print(d1.sound())
print(c1.sound())
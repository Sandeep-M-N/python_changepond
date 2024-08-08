#Task :
# Create an abstract class Car which will have abstract methods related to a
# car functionality(start_engine,stop_engine_drive)
# Implement concrete subclasess(ElectricCar,GasolineCar)
# Use the concrete subclasess (operate_car)

from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class ElectricCar(Car):

    def start_engine(self):
        return ("electric car start")
    
    def stop_engine(self):
        return ("electric car stop")
    

class GasolineCar(Car):
    
    def start_engine(self):
        return ("Gasoline car start")

    def stop_engine(self):
        return ("Gasoline car stop")
    

e1= GasolineCar()
g1=ElectricCar()
print(e1.start_engine())
print(e1.stop_engine())
print(g1.start_engine())
print(g1.stop_engine())
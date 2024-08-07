#public : These are accessible from outside the class
#protected: single underscore within the class and its subclass
#private: double underscore ,cannot be accessed outside the class

class Employee:
    def __init__(self,name,salary):
        self.name= name
        self._salary =salary  #protected attribute

    def DisplaySalaryInfo(self):
        print(f'{self.name} holding salary of {self._salary}')

    

e1 = Employee("Sandeep",25000)
print(e1.name)
print(e1._salary)
e1.DisplaySalaryInfo()
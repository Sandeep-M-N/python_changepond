#creating class
class Student:
    graduation="B.tech" # class variable
    def __init__(self,firstname,lastname):
        self.firstname = firstname  # instance variable #properties
        self.lastname = lastname
    
    # def display(self):  #instance method
    #     print(f'{self.firstname} {self.lastname}')

obj1= Student("sandeep","Rao")
# print(obj1.firstname)
# obj1.display()
print(obj1.graduation)
print(obj1.__class__.graduation)
class Student:

    # @staticmethod
    def RollNumber(y):
        print("inside static method",y)

#static method call
# Student.RollNumber(101)

#another way
Student.RollNumber=staticmethod(Student.RollNumber)
Student.RollNumber(102)

# using object
s1=Student()
s1.RollNumber(101)


# class method
class Student:
    graduation="B.tech" # class variable

    def graduation_info(cls):
        print("Graduation in : ", cls.graduation)
Student.Graduate= classmethod(Student.graduation_info)
Student.Graduate()

# another way
class Student:

    graduation="B.tech" # class variable
    @classmethod
    def graduation_info(cls):
        print("Graduation in : ", cls.graduation)

Student.graduation_info()

# 6)Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value1,Value2.
# Inside init method initialize all instance variables to 0.
# There are three instance methods inside class as Accept(),Addition(),Subtraction(),Multiplication(),Division().
# Accept method will accept value of value1 and value2 from user.
# Addition() method will perform addition of Value1 and Value2 and return result.
# Subtraction() method will perform subtraction of Value1 and Value2 and return result.
# Multiplication() method will perform multiplication of Value1 and Value2 and return result.
# Division() method will perform division of Value1 and Value2 and return result.
# After Designing the above class call all instance methods by creating multiple objects.

class Arithmetic:
    def __init__(self):
        self.val1=0
        self.val2=0
    def Accept(self):
        value1=int(input("enter the value1: "))
        value2= int(input("Enter the value2: "))
        self.val1=value1
        self.val2=value2
    def Addition(self):
        add=self.val1+self.val2
        return add
    def subtraction(self):
        sub=self.val1-self.val2
        return sub
    def Multiplication(self):
        mul = self.val1*self.val2
        return mul

    def Division(self):
        div = self.val1// self.val2
        return div
    
def main():
    obj1=Arithmetic()
    while True:
        print()
        print("1 For Addition")
        print()
        print("2 for subtraction")
        print()
        print("3 For Multiplication")
        print()
        print("4 For Division")
        print()
        choice = int(input("Enter the choice: "))
        if (choice==1):
            obj1.Accept()
            add1=obj1.Addition()
            print("ans is: ",add1)
        elif(choice==2):
            obj1.Accept()
            sub1=obj1.subtraction()
            print("ans is: ",sub1)

        elif(choice==3):
            obj1.Accept()
            mul1=obj1.Multiplication()
            print("ans is: ",mul1)

        elif(choice==4):
            obj1.Accept()
            div1=obj1.Division()
            print("ans is: ",div1)

        else:
            print("you have entered a wrong choice")
            break

if __name__=="__main__":
    main()


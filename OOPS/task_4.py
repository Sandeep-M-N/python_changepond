# 3)Write a program which contains one class named as Circle
# Circle class contains three instance variables as Radius,Area ,Circumference.
# That class contains one class variable as PI which is initialize to 3.14
# Inside init method initialize all instance variables to 0.0
# There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference( ),
# ,Display( )
# Accept method will accept value of Radius from user.
# CalculateArea () method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference () method will calculate circumference of circle and store it into instance variable
# Circumference.
# And Display( ) method will display value of all the instance variables as radius , Area , Circumference.
# After designing the above class call all instance methods by creating multiple objects
 

class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.circumference=0.0
    def Accept(self):
        input1=int(input("enter the radius: "))
        self.Radius=input1
        print("your radis is: ",self.Radius)

    def CalculateArea(self):
        AreaOfCircle= Circle.PI*self.Radius*self.Radius
        print("area of the circlke is: ",AreaOfCircle)
    def CalculateCirumference(self):
        CircumferenceOfCircle=2*Circle.PI*self.Radius
        print("circumferemnce of circle is: ",CircumferenceOfCircle)
    def Display(self):
        self.Accept()
        self.CalculateArea()
        self.CalculateCirumference()

def main():
    circle=Circle()
    circle.Display()

if __name__=="__main__":
    main()

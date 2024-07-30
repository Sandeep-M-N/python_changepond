import datetime
today=datetime.date.today()
year= today.year
class Company:
    area = "sipcot, siruseri"
    city="chennai"
    def __init__(self,cname) :
        self.cname= cname
    def displayCname(self):
        print("company Name: ",self.cname)
    def Address(self):
        return self.area + ','+self.city + " TamilNadu"
class Employee:
    empCount=0
    isMarried=False

    def __init__(self,fname,lname,yob,address):
        self.fname=fname
        self.lname=lname
        self.yob=year-yob
        self.address=address
        Employee.empCount+=1
     
        self.id=self.empCount

    def empdetails(self):
        print("Employee id: ",self.id)
        print("your fullname is: ",self.fname,"",self.lname)

        print("your age is : ",self.yob)
        if(self.yob>25):
            Employee.isMarried=True
        else:
            Employee.isMarried=False
        print("is Married: ",self.isMarried)
    def address(self):
        print()

e1=Employee("Sandeep","Rao",2001,"chenai,TamilNadu")
e1.empdetails()

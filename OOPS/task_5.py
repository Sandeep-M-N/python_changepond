# 4) Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That Class Contains one class variable as ROI which is initialize to 10.5
# Inside init method initialize all name and amount variable by accepting the values from user.
# There are four instance methods inside class as Display() , Deposit (), Withdraw( ), CalculateInterest()
# Deposit( ) method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateInterst() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI
# And Display () method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects

class BankAccount:
    ROI = 10.5
    
    def __init__(self):
        self.Name = ""
        self.Amount =1000
   

    def deposit(self,depositamount):
      
        self.Amount+=depositamount
        print("your total amount after deposit is: ",self.Amount)
    def withdraw(self, withdrawamount):
        
        self.Amount-=withdrawamount
        print("your  total amount aftervwithdrawl is: ",self.Amount)

    def CalculateInterest(self):
        interest=(BankAccount.ROI*self.Amount)//100
        print("your total interest is : ",interest)
    
    def display(self):
        name=input("Enter the Account Holder Name: ")
        amount=int(input("enter the amount: "))
        self.Name=name
        self.Amount=amount

    @staticmethod
    def displayKYCinfo(aadhar,photo):
        print("submit your aadhar: ",aadhar)
        print("submit your 2passport size photo",photo)

def main():
    bank=BankAccount()
    # bank.display()
    bank.deposit(500)
    bank.withdraw(300)
    # bank.CalculateInterest()
    # bank.displayKYCinfo(4767978657632,"demo.jpg")

if __name__=="__main__":
    main()

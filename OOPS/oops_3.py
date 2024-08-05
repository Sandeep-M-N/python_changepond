#instance variable : Name,Amount,Address,Account No
#instance method : CreateAccount(), displayAccountinfo()

class Bank:
    Bank_Name="Yes Bank"
    ROI_On_FD="15%"
    def __init__(self):
       self.Name = ""
       self.Amount = 0
       self.Address = ""
       self.AccountNo=0

    def CreateAccount(self):
        self.Name= input("enter your name: ")
        self.Amount= int(input("enter the initial amount: "))
        self.Address = input("enter the  address: ")
        self.AccountNo= int(input("Enter your account no: "))
    def DisplayAccountInfo(self):
        print("-------Below are the details of your account----------")
        print()
        print("your bank name is :",Bank.Bank_Name)
        print()
        print("your rate of interest is: ",Bank.ROI_On_FD)
        print("your account name is : ",self.Name)
        print()
        print("your initial amount is : ",self.Amount)
        print()
        print("your Address is : ", self.Address)
        print()
        print("your account no is : ",self.AccountNo)

    @classmethod
    def Bank_info(cls):
        print("your bank name is ",cls.Bank_Name)
        print("your rate of interest is ",cls.ROI_On_FD)
def main():
    # obj1=Bank()
    # obj1.CreateAccount()
    # obj1.DisplayAccountInfo()
    Bank.Bank_info()


if __name__=="__main__":
    main()


        
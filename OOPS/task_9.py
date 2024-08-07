class Shopping:
    cart=[]
    count=0
    items=["iphone","samsung","poco","oneplus","xiaomi","vivo","oppo","iqoo"]
    prices=[80000,75000,15000,39999,25000,22000,21000,19000]

    def __init__(self):
        self.price=0
    def additem(self):
        user=input("enter the item you have to add: ")
        index=Shopping.items.index(user)
        Shopping.cart.append(user)
        self.price+=Shopping.prices[index]
        print("item added sucessfully")

    def removeitem(self):
        removeuseritem=input("Enter the item to remove: ")
        index=Shopping.items.index(removeuseritem)
        Shopping.cart.remove(removeuseritem)
        self.price-=Shopping.prices[index]
        print("item removed successfully")



    def totalitems(self):
        Shopping.count=len(Shopping.cart)
        print("your total item are: ",Shopping.count)

    def totalprice(self):
        print("your total price is: ",self.price)

def main():
    obj1=Shopping()
   
   
    while True:
        print("----items    Price----")
        for i in range(len(obj1.items)):
            print(f'{obj1.items[i]}    {obj1.prices[i]}')

        print()

        print("1.Add item")
        print("2.remove item")
        print("3.total item")
        print("4.total price")
        print()
        choice = int(input("enter the choice: "))
        if(choice==1):
            obj1.additem()

        elif(choice==2):
            obj1.removeitem()

        elif(choice==3):
            obj1.totalitems()

        elif(choice==4):
            obj1.totalprice()

        else:
            print("you have entered a wrong choice ")
            break

if __name__=="__main__":
    main()

        

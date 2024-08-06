class MenuList:
    menulist=[]
    pricelist=[]
    
    def __init__(self):
        self.menuitem=""
        self.itemprice=0

    def displayitem(self):
        for i in range(len(MenuList.menulist)):
            print(f'   {MenuList.menulist[i]}    {MenuList.pricelist[i]}')

    def Additem(self):
        addmenu=input("enter the item to add: ")
        addprice=int(input("enter the price to add: "))
        self.menuitem=addmenu
        self.itemprice=addprice
        MenuList.menulist.append(self.menuitem)
        MenuList.pricelist.append(self.itemprice)
        print("-----item and price added successfully-----")

    def updateitem(self):
        pastitem=input("Enter the pastitem to update: ")
        newitem=input("Enter the newitem to be added in the pastitem: ")
        newprice=int(input("Enter the new Price: "))
        self.menuitem=newitem
        self.itemprice=newprice
        itemindex=MenuList.menulist.index(pastitem)
        MenuList.menulist[itemindex]=self.menuitem
        MenuList.pricelist[itemindex]=self.itemprice
        print("-----item updated successfully-----")

    def removeitem(self):
        ritem=input("Enter the item to be removed: ")
        rindex=MenuList.menulist.index(ritem)
        MenuList.menulist.pop(rindex)
        MenuList.pricelist.pop(rindex)
        print("----item removed successfully-----")






def main():
    obj1=MenuList()
    while True:
        print()
        print("1.Display menu list")
        print("2.Add in the menu list")
        print("3.update menu list")
        print("4.Remove menu list")
        print()
        choice=int(input("enter the choice: "))
        print()
        if(choice==1):
            print("------ItemList      Price----")
            obj1.displayitem()
        elif(choice==2):
           obj1.Additem()

        elif(choice==3):
            obj1.updateitem()

        elif(choice==4):
            obj1.removeitem()

        else:
            print("you have entered a wrong choice")
            break

if __name__=="__main__":
    main()



class Product:
    product_id=0
    def __init__(self,Pname,Pprice):
        self.Pname=Pname
        self.Pprice=Pprice
        Product.product_id+=1
        self.id=self.product_id
    def AddProducts(self,Pname,Pprice):
        self.name_list=[]
        self.product_id=[]
        self.price_list=[]
        name_list.append(Pname)
        product_id.append(self.id)
        price_list.append(Pprice)


    def productDetails(self,display_id):
       print("your product ")


while True:
    print("Display Choices:")
    print()
    print("1.Add products ")
    print("2.Display Product Details ")
    print()
    choice= int(input("Enter the Choices"))
    if(choice==1):
        Pname=input("Enter The Product Name: ")
        Pprice=int(input("Enter The product Price: "))
        Product.AddProducts(Pname,Pprice)
    elif(choice==2):
        print("Enter the id to displayed")
        display_id=int(input())
        Product.productDetails(display_id)



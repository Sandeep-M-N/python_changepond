class Product:
    product_id=0
    name_list=[]
    product_id=[]
    price_list=[]
    def __init__(self,Pname,Pprice):
        self.Pname=Pname
        self.Pprice=Pprice
        Product.product_id+=1
        self.id=self.product_id
    def AddProducts(self,Pname,Pprice):
       
        Product.name_list.append(Pname)
        self.product_id.append(self.id)
        Product.price_list.append(Pprice)


    def productDetails(display_id):
       print("product Id id : ",Product.product_id[display_id-1])
       print("product name is : ",Product.name_list[display_id-1])
       print("product price is : ",Product.price_list[display_id-1])



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
       
    else:
        print("you have entered a wrong choice")



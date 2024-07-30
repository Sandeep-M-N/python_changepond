def order_sandwich(*args):
 while True:
    name = input("Enter your Name : ")
    print("list of sandwiches")
    print("1.veg sandwich")
    print("2.veg cheesy sandwich")
    print("3.mushroom sandwich")
    print()
    sandwich_choice=int(input("enter the choice : "))
    print()
    print("list of toppings")
    print("1.corn")
    print("2.cheese")
    print("3.mayoniese")
    print()
    topping_choice=int(input("enter the toppings to be added : "))
    print()
    for i in args[0]:
       if (args[0][sandwich_choice-1]==i):
          for j in args[1]:
             if(args[1][topping_choice-1]==j):
                print(f' {name} selected {i} with {j}')
                print()




def main():
      order_sandwich(["veg sandwich","veg cheesy sandwich","mushroom sandwich"],["corn","cheese","mayoniese"])

if __name__=="__main__":
    main()
def order_sandwich(*args):
 while True:
    print("list of sandwiches")
    print("1.veg sandwich")
    print("2.veg cheesy sandwich")
    print("3.mushroom sandwich")
    sandwich_choice=int(input("enter the choice"))
    print("list of toppings")
    print("1.corn")
    print("2.cheese")
    print("3.mayoniese")
    topping_choice=int(input("enter the toppings to be added"))
    for i in args[0]:
       if (args[0][sandwich_choice-1]==i):
          for j in args[1]:
             if(args[1][topping_choice-1]==j):
                print(f'selected {i} with {j}')




def main():
    while True:
        
        order_sandwich=(["veg sandwich","veg cheesy sandwich","mushroom sandwich"],["corn","cheese","mayoniese"])

if __name__=="__main__":
    main()
# 1) Create a menu_card list
# veg_starter = ['paneer 65','chilly paneer','veg crispy']
# 1) Display menu card
# 2)Add Starter in the menu card
# 3)Update Starter in the menu card
# 4)Remove Starter in the menu card
 
# Example:
# Add : Which starter you want to add in menu?
# paneer roll
# ['Paneer 65','Chilly paneer','Veg crispy','Paneer roll']
# Added Successfully


def add_funtion(menu_list,add_list,index):
    menu_list[index]=add_list
    return menu_list
def update_function(menu_list,update_list,update_item):
    menu_list[update_list]=update_item
    return menu_list
def remove_function(menu_list,remove_list):
   return menu_list.pop(remove_list)
    
def main():
    menu_options={
        1 : "Dispaly menu list",
        2 : "Add on the menu list",
        3 : "Update on the menu list",
        4 : "remove from the menu list"
    }
    menu_list={}
    index=0
    size=int(input("Enter the Size: "))
    for i in range(size):
        key=index
        item=input("Enter the item: ")
        menu_list[key]=item
        index+=1
        
    
    
    
    while True:
        print()
        print(menu_options)
        print()
        choice=int(input("enter your choice: "))

        if(choice==1):
            print(menu_list)
            continue
        elif(choice==2):
            add_list=input("which starter do you want to add in the menu: ")
            print(add_funtion(menu_list,add_list,index))
            index+=1

            
        elif(choice==3):
            update_list=int(input("enter the index to be update: "))
            update_item=input("enter the item")
            print(update_function(menu_list,update_list,update_item))
        
        elif(choice==4):
            remove_list=int(input("enter the index to be removed: "))

            print(remove_function(menu_list,remove_list))
            for i in range(remove_list,len(menu_list)):
                menu_list[remove_list]=menu_list[remove_list+1]
                remove_list+=1
            index=remove_list
            menu_list.pop(remove_list)
            sorted(menu_list)

                    
            
            print(menu_list)
            
            
        else:
            print("you have enter the wrong choice")
            break


# maps = {0:"1",2:"2",1:"1"}
# keys=list(maps.keys())
# keys.sort()
# maps={i:maps[i] for i in keys}
# print(maps)









if __name__=="__main__":
    main()
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


def add_funtion(menu_list,add_list):
    menu_list.append(add_list)
    return menu_list
def update_function(menu_list,update_list,update_item):
    menu_list[update_list]=update_item
    return menu_list
def remove_function(menu_list,remove_list):
    menu_list.remove(remove_list)
    return menu_list
def main():
    menu_list=["paneer 65","Chilly chicken","veg crispy"]
    choice=int(input("enter your choice"))
    while(True):
        if(choice==1):
            print(menu_list)
            break
        elif(choice==2):
            add_list=input("which starter do you want to add in the menu")
            print(add_funtion(menu_list,add_list))
            break
        elif(choice==3):
            update_list=int(input("enter the index to be update"))
            update_item=input("enter the item")
            print(update_function(menu_list,update_list,update_item))
            break
        elif(choice==4):
            remove_list=input("enter the item to be removed")
            print(remove_function(menu_list,remove_list))
            break
        else:
            print("you have enter the wrong choice")
            break









if __name__=="__main__":
    main()
# 9-1. Restaurant: Make a class called Restaurant. The _init_() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.


class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type


    def describe_restaurant(self):
        print("SERVED EVERY DAY SINCE 1990")
        print("SAY NO TO MEATS ON DRUGS")

    def restaurant_open(self):
        print("restaurant is open")

def main():   
    obj1=Restaurant("Taco Bell","Multi-Cuisine")
    obj2=Restaurant("Hotel Sherva","Multi-cuisine")
    obj3=Restaurant("Hotel Lingam","Veg-Restaurant")
    print(obj1.restaurant_name)
    print(obj1.cuisine_type)
    obj1.describe_restaurant()
    obj2.describe_restaurant()
    obj3.describe_restaurant()
    obj1.restaurant_open()
            
if __name__=="__main__":
    main()
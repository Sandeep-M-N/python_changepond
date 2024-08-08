# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.


class User:
    
    def __init__(self,first_name,last_name,age,company_name,domain):
        self.fisrt_name=first_name
        self.last_name=last_name
        self.age=age
        self.company_name=company_name
        self.domain=domain

    def describe_user(self):
        print(f'my Name is {self.fisrt_name} {self.last_name} My age is {self.age} I am working in {self.company_name} and I am a {self.domain} ')


    def greet_user(self):
        print("welcome to our Chanepond Technologies")

def main():
    obj1=User("Sandeep","Rao",22,"Changepond Technologies","software developer")
    obj2=User("Basil","Ahmad",21,"Changepond Technologies","software developer")
    obj3=User("Siva","lingam",22,"ChangePond Technologies","Dot Net Tester")

    obj1.describe_user()
    obj1.greet_user()
    obj2.describe_user()
    obj2.greet_user()
    obj3.describe_user()
    obj3.greet_user()

if __name__=="__main__":
    main()


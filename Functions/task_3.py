# 3 Question:Create a simple calculator which will take two input number from the
# user and give following option
# 1)Addition
# 2) Subtraction
# 3)Multiplication
# 4)Division
# (you can solve above question using normal function )
# (also try to solve using dictionary)

import task_3arithmetic

print("choices")
print("1-> Addition")
print("2-> subtraction")
print("3-> Multiplication")
print("4-> Division")
choice = int(input("enter the choice : "))

def main():
    value1=int(input("Enter the value1: "))
    value2=int(input("Enter the value2: "))

    while(True):
        if(choice==1):
           print(task_3arithmetic.add_function(value1,value2))
           break
        elif(choice==2):
            print(task_3arithmetic.sub_function(value1,value2))
            break
        elif(choice==3):
            print(task_3arithmetic.mul_function(value1,value2))
            break
        elif(choice==4):
            print(task_3arithmetic.div_function(value1,value2))
            break
        else:
            print("you have entered the wrong choice")
            break

    



if __name__=="__main__":
    main()
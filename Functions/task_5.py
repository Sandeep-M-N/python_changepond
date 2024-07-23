# 5 question:Write a program to check if a string contains any special character
def special_function(String):
    specialCharacter="!@#$%&?"
    dummystring=""
    for i in specialCharacter:
        if i in String:
            print(i)
def main():
    String=input("enter the string: ")
    special_function(String)



if __name__=="__main__":
    main()
import datetime
today = datetime.date.today()
year = today.year


# try:
#     num1= int(input("enter the number 1 : "))
#     num2= int(input("Enter the number 2 : "))
#     assert num1%2==0
#     result=num1/num2
#     print(result)
# except ZeroDivisionError:
#     print("Error: Denominator cannot be zero")
# except ValueError:
#     print("only integers are allowed")
# except AssertionError:
#     print("enter value is not matching the test condition")
# else:
#     print(num1,"is even")
# finally:          if error has happen(that is in the except) or not happened finally will execute 
#     print("program is over")

yob = int(input("enter your year of birth : "))
age = year - yob
if(age < 18):
    raise Exception(f'the age should be grater than 18 and your age is {age}')
print(age)
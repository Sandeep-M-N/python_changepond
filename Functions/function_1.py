# def Addition():
#     print("inside addition") # no parameter ,No arguement 
# Addition()

# def Addition(value1):
#     print(value1)
# Addition(12)

# def Addition(value1,value2):
#     print(value1+value2)
# Addition(12,13)

def Addition(value1,value2):
    add=value1+value2
    sub=value1-value2
    return (add,sub)
add,sub = Addition(12,13)
print(add,'\n',sub)

# def subtraction(val1,val2):
#     return val1 - val2
# print(subtraction(20,10))

# creating a  set
staff_id = {123,124,125,126} # same data type
mixed_type = {"sandeep",124,25,True,124} # mixed data type
print(mixed_type) #output will come in randomly not in orderly manner
print(len(mixed_type))

#set considers
#True -1
#False -0
s1 = {True,0,1,False}
print(s1)


#task -> iterate using for loop
for index in mixed_type:
    print(index)

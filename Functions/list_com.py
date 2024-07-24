# list1=[]
# size=int(input("enter the size: "))
# for i in range(size):
#     value=i*i
#     list1.append(value)
# print(list1)

# using list  comprehensio creating a list of square numbers

#new_list = [expression for member in iterable]

#new_list = [expression for member in iterable if(optional)]

new_list = [i for i in range(1,11)]
print('list comprhension:',new_list)

new_list = [i for i in range(1,11) if(i%2==0)]
print('list comprhension:',new_list)

#task try out u r name and filter out the vowels
string = "aeiou"
name="sandeep"
new_list=[i for i in name if i in string]
print(new_list)
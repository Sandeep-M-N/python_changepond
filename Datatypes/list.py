#creating a list
# homogenous
course = ['python','java','php'] # string
rollno= [123,456,789] # integer

# creating mixed type
#heterogenous
# mixed_type = ['sandeep',123,True,67.68]
# print('length :',len(mixed_type))
# print('index of 123 :',mixed_type[1])
# print('index of 68 :',mixed_type[-3])

#slicing : [start:stop(excuded)]
# print('slicing :',mixed_type[1:3])



# print('slicing :',mixed_type[-4:-1])

#Mutable (can change,add and delete)

fruits = ['Mango','Banana','Grapes','Watwermelon']
fruits[1]='Avacado'
print(fruits)
del fruits[len(fruits)-1]
print(fruits)
#slcing replaced avacado,grapes ->
fruits[1:3]=['banana','orange']
print(fruits)
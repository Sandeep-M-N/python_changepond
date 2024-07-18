# create a tuple
#homogenous
student_id = (123,124,124,126)
ice_cream = ('vanilla','choco-chips','Blueberry')

# heterogenous 
mixed_type= (123,'hello',False,56.78)
print(len(ice_cream))
print(ice_cream[len(ice_cream)-1])
print(mixed_type[-2])
print(mixed_type[1:3])

ice_cream = ('vanilla') # str
print(ice_cream,type(ice_cream))
ice_cream = ('vanilla',) # tuple
print(ice_cream,type(ice_cream))

#methods 
ice_cream=('vanilla','choco-chips','Blueberry','vanilla')
#count method
count_menthod=ice_cream.count('vanilla')
print(count_menthod)
print()
#index method
index_method = ice_cream.index('vanilla')
print(index_method)
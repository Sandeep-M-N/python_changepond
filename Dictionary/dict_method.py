watch_details = {
    'titan':8000,
   'fastrack':9000,
    'omega':9000,
    'titan':12000
}
#keys() -> returns  a list containing the dictionary's keys
key_method=watch_details.keys()
print(key_method)

# values()
value_method = watch_details.values()
print(value_method)

#get method - > returns the value of specified key
get_method = watch_details.get('titan')
print(get_method)

# items() methods - > returns a tuple inside a list
item_method = watch_details.items()
print(item_method)

#update method -> insert an item to an dictionary
watch_details.update({'noise':15000})
print(watch_details)


#pop() -> remove element with the specified key
watch_details.pop('titan')
print(watch_details)
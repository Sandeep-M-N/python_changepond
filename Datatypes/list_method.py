menu_card = ['paneer','dal','rice']
print(menu_card)

#append() -> adds an element at the end of the list
menu_card.append('dosa')
print(menu_card)
# extend() - > add the element of the list(or iterable) to the end of the list
menu_card.extend(['poori','pongal'])
print(menu_card)
#insert -> adds an element at the specified position
menu_card.insert(1,'veg birinji')
print(menu_card)

#remove() -> it will remove specified value
menu_card.remove('poori')
print(menu_card)

#pop() -> removes element of specified position
menu_card.pop(2)
print(menu_card)
#index method
print(menu_card.index('rice'))
#sort method
menu_card.sort()
print(menu_card)
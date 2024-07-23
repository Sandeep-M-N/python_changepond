mixed_type = {"sandeep",124,25,True,124}
more_add={"rahul",34}

#add() -> add element to the set
mixed_type.add("developer")
print(mixed_type)

#updat() -> update element combines another set and updates in  one set

mixed_type.update(more_add)
print(mixed_type)

#discard() -> it removes an particular element
mixed_type.discard("developer")
print(mixed_type)

#remove() -> it removes an particular element
mixed_type.remove(124)
print(mixed_type)

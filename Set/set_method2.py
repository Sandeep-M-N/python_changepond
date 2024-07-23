company = {'Microsoft','standard charted','freshworks','comcast'}
add_company = {'Yes bank','comcast','Microsoft','freshworks'}


# union method 
# union_method = company.union(add_company)
# print(union_method)

# union method using operator
union_method = company | add_company
print(union_method)

# intersection method 
intesect_method = company.intersection(add_company)
print(intesect_method)

# difference method() it will subtract the common values in both set and display the values that is in
# the first set(what set is in left side of the set)
difference_method = company.difference(add_company)
print(difference_method)
 
#symmetric method() ->  it will subtract the common values in both set and display the values that is in
# the both set
symmetric_method = company.symmetric_difference(add_company)
print(symmetric_method)
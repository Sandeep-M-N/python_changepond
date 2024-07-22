#f-string (insert a variable's name into a string, place the letter f immediately before opening the quotation mark
# put braces around the variable names
# python will replace each variable with its value when string is displayed
# these string are called as f-string
# f-stirng were introduced in python - 3.6)
student_name = input("enter u r name:")
student_id = int(input("enter you id card number"))
# print(f'student name {student_name.title()} \n student id : {student_id}')
# print(f'student name {student_name.upper()} \n student id : {student_id}')
# print(f'student name {student_name.lower()} \n student id : {student_id}')

#format method
print('student name {} \n student id : {}'.format(student_name,student_id))
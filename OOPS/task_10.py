import os
 
def task():
    if os.path.exists(r"C:\Users\sandeep.mn\Documents\sandeep\Python\OOPS\demo.text"):
        permission = open(r"C:\Users\sandeep.mn\Documents\sandeep\Python\OOPS\demo.text","r")
        content = permission.read()
        lists = content.split(" ")
        checking = input("ENter the search words: ")
        if checking in lists:
            return f"the {checking} is present in the file"
        else:
            return f"the {checking} is not present in the file"
    else:
        print("Dont Have file")
print(task())
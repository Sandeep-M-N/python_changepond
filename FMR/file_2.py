#open() function -> filename,mode(r,w,a....)
# file_read = open('lambda_1.py','r')
# print(file_read.read())
import os
def CreateFile(file_name): #filename = calculator_grade.py
    if(os.path.exists(file_name)):
        print("file name is already exists")
    else:
        file_create=open(file_name,'w')
def main():
    print("enter the file name you want to create")
    file_name=input()

    CreateFile(file_name)

if __name__=="__main__":
    main()
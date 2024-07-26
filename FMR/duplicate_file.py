import os
import filecmp
def comparefiles(file1,file2):
    if(not os.path.exists(file1)):
        print("file1 not found",file1)
    elif(not os.path.exists(file2)):
        print("file2 not found",file2)
    else:
        compare=filecmp.cmp(file1,file2)
        if compare==True:
            os.remove(file2)
            print("one of the file is deleted")
        else:
            print("the files are different")
def main():
    file_1=input("enter the first file name: ")
    file_2=input("enter the second file name: ")
    comparefiles(file_1,file_2)
if __name__=="__main__":
    main()
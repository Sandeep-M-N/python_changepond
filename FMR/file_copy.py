import os
import filecmp
def createFile(file1,file2):
    # for i in file_read:
    #     file_create.write(i)
    # print("all contents are copied")
    # file_compare(file_read,file_create)
    if(os.path.exists(file1)):
         if(not os.path.exists(file2)):
               file_read=open(file1,'r')
               file_create=open(file2,'w')
               data_read=file_read.read()
               data_copy=file_create.write(data_read)
               print("all contents are copied")
         else:
          compare=filecmp.cmp(file1,file2)
          if compare==True:
            print("both files are same")
          else:
            print("the files are different")
         




def main():
   file1=input("enter the file name: ")
   file2=input("enter the new file name")
#    file_read=open(file1,'r')
#    file_create=open(file2,'w')
   createFile(file1,file2)


if __name__=="__main__":
    main()
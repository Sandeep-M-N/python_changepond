import os
def delete_file(filename):
    if(os.path.exists(filename)):
        os.remove(filename)
        print("file is successfuly removed")
    else:
        print("filename does not exist")

def main():
    filename=input("enter the filename: ")
    delete_file(filename)


if __name__=="__main__":
    main()
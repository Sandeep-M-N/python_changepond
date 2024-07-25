#write a program which will check the number is greater and equal to 70
# and less than and equal to 90
# def checkNumber(Number):
#     if(Number>=70 and Number<=90):
#         return Number
def filtered(string):
   
    for i in string:
        if(len(string)==0):
            return False
        else:
            return True
       
def mapped(val1):
    special="'' ,;."
    var=""
    for i in val1:
        if i not in special:
            var+=i
    return var
    
def main():
    # size = int(input("enter the size: "))
    # list1=[]
    # print("enter values: ")
    # for i in range(size):
    #     value = input()
    #     list1.append(value)
    # print("user list : ",list1)

    # filter_list=list(filter(checkNumber,list1))
    # print(filter_list)
    list1=['','java',',','.','angu;lar','python']
    map_list=list(map(mapped,list1))
    filter_list=list(filter(filtered,map_list))
    
    print(filter_list)
    

if __name__=="__main__":
    main()

from functools import reduce
def main():
    size = int(input("enter the size: "))
    list1=[]
    print("enter values: ")
    for i in range(size):
        value = int(input())
        list1.append(value)
    print("user list : ",list1) #[3,4,5,6]

    map_list=list(map(lambda num : num**3,list1)) #[27,64,125,216]
    print(map_list)
    print()
    reduce_list=reduce((lambda num1,num2:num1+num2),map_list)
    print(reduce_list)
    #running of reduced list
    #num1-27,num2-64 = 91
    # num1-91,num2-125 = 216
    # num1-216,num2-216 = 432
    

if __name__=="__main__":
    main()
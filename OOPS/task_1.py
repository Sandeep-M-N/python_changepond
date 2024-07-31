from random import random
def main():
    val1=int(random()*10000)
    print(val1)
    String=str(val1)
    String2 = String[::-1]
    val2=int(String2)
    rem=0
    list1=[]
    index=0
    while(val2!=0):
        rem=val2%10
        list1.append(rem)
        val2//=10
    print(list1)
    cow=0
    bull=0
    while True:
        digit=int(input("Enter the number: "))
        for i in range(len(list1)):
            if (list1[index]==digit):
                cow+=1
                
                
                index+=1
            else:
                for j in list1:
                    if digit==j:
                        bull+=1
        print("cow: ",cow)
        print("bull: ",bull)                






if __name__=="__main__":
    main()
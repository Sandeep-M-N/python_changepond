# 4 question:Write a program which will count the frequency of letters of the string

def main():
  String=input("enter the string: ")
  for i in range(len(String)):
  
    count=1
    if(index==len(String)):
       print(f'{String[index]} is repeated {count}')
    else:
        for j in range(index+1,len(String)):
            if(String[i]==String[j]):
                count+=1
        print(f'{String[i]} is repeated {count}')





if __name__=="__main__":
    main()

#dynamic input
def count_sum(data_input,search_num):
    count=0
    for i in data_input:
        if(i==search_num):
            count+=1
    return count


def main():
    print("enter the element you want to enter in the list")
    size = int(input()) 
    data_input=[]
    print("enter the values:")
    for i in range(size):
        value=int(input())  #[2,3,4,2,4,5]
        data_input.append(value)
    search__num = int(input('Enter the element to search in the check list:'))
    print(search__num,"is repeating", count_sum(data_input,search__num))
    

if __name__=="__main__":
    main()
def total_marks(list1,grade):
    total=0
    for i in list1:
        total+=i
    print("total marks: ",total)

    if(total>=450 and total<=500):
        return grade[450]
    elif(total>=400 and total<=449):
        return grade[400]
    elif(total>=350 and total <=399):
        return grade[350]
    elif(total>=300 and total<=349):
        return grade[300]
    else:
        return grade[299]





def main():
   grade = {
       450:"O",
       400:"A",
       350:"B",
       300:"C",
       299:"D"
   }
   
   list1=[]
   size= int(input("enter the size"))
   fullmarks=0
   print("enter marks: ")
   for i in range(size):
       value=int(input())
       list1.append(value)
   print(list1)
   print(total_marks(list1,grade))





if __name__ == "__main__":
    main()
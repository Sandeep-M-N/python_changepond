# 5)Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialize that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false
# ChkPerfect () method will returns true if number is perfect otherwise return false.
# Factors () method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# As a helper method if required.
# After Designing the above class call all instance methods by creating multiple objects.



class Numbers:
    

    def __init__(self):
        self.value=0

    def chkPrime(self):
        count=0
        self.value=int(input("enter the value: "))
        num1=self.value
        if(num1==1 or num1==2):
            return(f'{self.value} is a Prime number')
        
        num1=num1//2
       
        
        for i in range(2,num1):
            if(num1%i!=0):
                count=0
            else:
                count=1
        if(count==0):
            return(f'{self.value} is a prime number')
        else:
            return(f'{self.value} is not a prime number')


    def factors(self):
        list1=[]
          
        self.value=int(input("enter the value: "))
        
      
        
        for i in range(1,self.value+1):
            if(self.value%i==0):
                list1.append(i)
       
        return list1
    
    def sum_of_factors(self):
        
        sum=0
        self.value=int(input("enter the value: "))
        
       
            
        
        
        for i in range(1,self.value+1):
            if(self.value%i==0):
                sum+=i
        
        return sum
    
def main():
    obj1=Numbers()
    while True:
        print("1.Check Prime")
        print("2.list all the factors")
        print("3.sum of factors")
        print()
        choice=int(input("Enter the  choice : "))
        if(choice==1):
            print(obj1.chkPrime())
            break
        elif(choice==2):
            print(obj1.factors())
            break
        else:
            print(obj1.sum_of_factors())
            break

    
if __name__=="__main__":
    main()
    
        

class Salary:
    def __init__(self,base_salary):
        self.base_salary=base_salary

class Allowances(Salary):
    def __init__(self, base_salary):
        super().__init__(base_salary)
        self.hra=(base_salary//100)*20
        self.da=(base_salary//100)*40
        self.ta=(base_salary//100)*25
    def getAllowances(self):
       
        allowance= self.hra + self.da + self.ta
        total_salary=self.base_salary + self.hra + self.da + self.ta
        
       
        return total_salary,allowance
    
class Deduction(Salary):
    def __init__(self, base_salary):
        super().__init__(base_salary)
        self.insurance=self.base_salary-5000
        
        self.pf=(self.base_salary//100)*12
        self.grati=(self.base_salary//100)*5

class CalculateSalarySlip(Allowances,Deduction):

    def netSalaryslip(self):
        print("your base salary is : ",self.base_salary)
        get_total_salary,get_allowance=self.getAllowances()
        print("your gross salary is : ",get_total_salary)

        netSalary=self.insurance + self.pf + self.grati
        print("your deduction amount is : ",netSalary)
        print("you allowance is : ",get_allowance)
        total_salary_amount=get_total_salary-netSalary
        print("your total salary after deduction : ",total_salary_amount)




base_salary=int(input("Enter the base salary: "))
s1=CalculateSalarySlip(base_salary)
s1.netSalaryslip()

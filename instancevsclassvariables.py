class Employee:
    company_name="Apple"
    noofEmpo=0
    def __init__(self,name,):
        self.name=name
        self.raise_amount=0.2
        Employee.noofEmpo+=1
        
    def showDetails(self):
        print(f"The name of the Employee {self.name} of {self.company_name} and the raise amount is {self.raise_amount} in sized {self.noofEmpo}")
        
emp1=Employee("Frank Das")
emp1.raise_amount=0.3
emp1.company_name="Intel"
emp1.showDetails()
# Employee.showDetails(emp1)    #from this we can understand one argument is going in showDetails()
Employee.company_name="AMD"
emp2=Employee("Harry Ali")
emp2.showDetails()

emp3=Employee("Rohan Das")
emp2.showDetails()
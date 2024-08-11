class Employee:
    company="Apple"
    def show(self):
        print(f"The name of the Employee is {self.name} and work in the company {self.company}")
    @classmethod     #changes the value of class variable   
    def changeCompany(cls,newCompany):
        cls.company=newCompany
        
e1=Employee()
e1.name="John"
e1.show()
e1.changeCompany("Tesla")
e1.show()

print(Employee.company)
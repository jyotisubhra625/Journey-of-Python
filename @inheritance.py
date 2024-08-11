class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee : {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print(f"The language of Employee {self.id} is Python")
e1=Employee("Rohan Das",420)
e1.showDetails()    
e2=Programmer("Frank Das",424)
e2.showDetails()
e2.showLanguage()
    
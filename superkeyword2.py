class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id=id
class Programmer(Employee):
    def __init__(self,name,id,lang):
        # self.name=name
        # self.id=id
        #instead using super to use the __init__ function as it also have self.name and self.id
        super().__init__(name,id)
        self.lang=lang
rohan=Employee("Rohan Das","421")
frank=Programmer("Frank Das","2345","Python")
print(frank.name)
print(frank.lang)
print(frank.id)
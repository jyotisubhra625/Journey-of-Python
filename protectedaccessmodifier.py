class Student:
    def __init__(self):
        self._name="Harry"
    def _funName(self):         #Protected method
        return "CodeWithHarry"
class Subject(Student):        #Inherited class
    pass
obj1=Student()
obj2=Subject()

#calling by object of Subject class
print(obj1._name)
print(obj1._funName)

#calling by object of Student class
print(obj2._name)
print(obj2._funName)


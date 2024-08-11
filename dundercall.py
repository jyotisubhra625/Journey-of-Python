# class Employee:
#     def __init__(self,name):
#         self.name=name
#     def __len__(self):
#         i=0
#         for c in self.name:
#             i=i+1
#         return i
from dundermthod import Employee

e=Employee("Frank")
# print(e)
print(len(e))
print(str(e))
print(repr(e))
e()
# print(e.name)
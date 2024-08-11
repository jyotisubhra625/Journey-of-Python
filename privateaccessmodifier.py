class Employee:
    def __init__(self):
        self.__name="Frank"    #private access modifier is indicated by "_ _"
a=Employee()
# print(a.__name)  by this method it cannot be accessed and will give error
print(a._Employee__name)
#by this private access modifier can also be accessed

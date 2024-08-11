class Person:
    name="Frank"
    occupation="Game Developer"
    networth=100000
    def info(self):
        print(f"{self.name} is a {self.occupation} of Net Worth {self.networth} ")
        # self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class
    
    
a=Person()
b=Person()
c=Person()
a.name="Subham"
a.occupation="Charterd Accountant"
a.networth=10000

b.name="Nikita"
b.occupation="Personal Assistant"
b.networth=20000

c.name="Sagnik"
c.occupation="Soft Developer"
c.networth=50000
'''if the above lines including a,b or c is commented out the default value of class Person is taken '''

# print(a.name,a.occupation,a.networth)

a.info()
b.info()
c.info()
class Person:
    # name="Frank"
    # occ="Developer"
    
    def __init__(self,n,o):
        # print("Hey I am a person")
        self.name = n
        self.occ=o
        
    def info(self):
        print(f"{self.name} is a {self.occ} ")
a=Person("Frank","Developer")
b=Person("Aditiya","HR")

# print(a.name)
# a.name="Diviya"
# a.occ="HR"
a.info()
b.info()    
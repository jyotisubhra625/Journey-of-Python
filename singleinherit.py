class Animals:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("Sound made by the animal")
        

class Dog(Animals):
    def __init__(self, name,breed):
        Animals.__init__(self,name,species="Dog")
        self.breed=breed
        
    def make_sound(self):
        print("Woof")
    def bark(self):
        print("Woof woof")
    def lick(self):
        print("Licking")

#Quick quiz:Implement a cat class by using the animal class add some methods specific to cat
class Cat(Animals):
    def __init__(self, name, breed):
        Animals.__init__(self, name, species="Cat")
        self.breed = breed
    def make_sound(self):
        print("Meow")
    def scratch(self):
        print("Scratching the furniture")
    def hiss(self):
        print("Hissing at the dog")
        
        
a=Animals("Dog","Lab")
a.make_sound()

d=Dog("Dog","Doberman")
d.make_sound()
d.bark()
d.lick()


c = Cat("Whiskers", "Siamese")
c.make_sound()
c.scratch()  
c.hiss()  
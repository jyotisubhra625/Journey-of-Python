class Parentclass:
    def parent_method(self):
        print("Parent method 1 called")
class Childclass(Parentclass):
    def parent_method(self):
        print("Parent Method 2 called")
        super().parent_method()
    def child_method(self):
        print("Child method called")
        super().parent_method()
        
child_object=Childclass()
child_object.child_method()
child_object.parent_method()

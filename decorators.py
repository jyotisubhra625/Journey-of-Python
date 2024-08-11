# decorator is a function that takes another function as an argument
                               #  and returns a new function that modifiesthe behavior of the orginal function
                               
    
def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this")
    return mfx

@greet
def hello():
    print("Hello")
# greet(hello)()

@greet  
def add(a,b):
    print("Sum is = ",(a+b))
    
hello()
greet(add)(1,2)
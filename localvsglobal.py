x=4          #global variable
print(x)


def hello():
    global x
    x=5     #local variable
    print(f"The local x is {x}")
    
    
print(f"The global x is {x}")
hello()
print(f"The global x is {x}")
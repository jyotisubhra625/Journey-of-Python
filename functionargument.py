def average(a,b):
    print("The Average is ",(a+b)/2)

a=int(input("Enter a number : "))
b=int(input("Enter a number : "))

average(a,b)

#default arguments
def average(a=10,b=2):        
    print("The Average is ",(a+b)/2)    #prints the average of a and b given inside the ( )

average()     # triggers the average of a and b given inside the ( )
average(1,6)  # prints the avergae of the value given inside its ( ) instead of the given value of default argument in the function
average(a=5)  # keeps the same value of b as in default argument but changes value of a
average(b=9)  # keeps the same value of a as in default argument but changes value of b


def name(fname,mname,lname):
    print("Hello Mr/Mrs",fname,mname,lname)
    print("First name: ",fname,)
    print("Middle name: ",mname,)
    print("Last name: ",lname,)

name("Narayan","Chandra","Das")



average(b=9,a=21)    #we can change the postion of the arguments 


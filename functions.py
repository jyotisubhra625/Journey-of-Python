#without function
a=9
b=8
gmean1=(a*b)/(a+b)
print(gmean1)
if(a>b):
    print("First number is greater")
elif(a==b):
    print("Both numbers are equal")
else:
    print("Second number is greater")

c=8
d=7
gmean2=(c*d)/(c+d)
print(gmean2)
if(c>d):
    print("First number is greater")
elif(c==d):
    print("Both numbers are equal")
else:
    print("Second number is greater")

#using function

def calculateGmean(a,b):   #def is used in user defined function
    mean=(a*b)/(a+b)
    print("Using function",mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    elif(a==b):
        print("Both numbers are equal")
    else:
        print("Second number is greater")
        def isLesser(a,b):
            pass                #makes the interpreter run the rest of the program
x=8
y=9
calculateGmean(x,y)
isGreater(x,y)

w=8
z=7
calculateGmean(w,z)
isGreater(w,z)


    


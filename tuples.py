t=(1,5,6,76,342,32,"green",True)    #tuples are ordered collection of data item and are unchangeable after creation
t1=(1)        #interpreter thinks it as int
t2=(1,)       #by adding a comma it makes the interpreter think it is a tuple
print(type(t))
print(type(t1))
print(type(t2))

#t[0]=90     #this gives error as tuple are unchanable after creation

print(t[0])
print(t[-1])
print(t[2])
#print(t[34])  #gives error

if 342 in t:
    print("342 is present in tuple")
else:
    print("342 is not present in tuple")

t1=t[1:4:2]
print(t1)
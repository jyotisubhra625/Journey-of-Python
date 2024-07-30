a="1"
print(type(a))
b="2"
print(type(b))
print(a+b)  #string


a1=1
print("\n",type(a1))
b1=2
print(type(b1))
print(a1+b1)   #integer

#Type casting

#Explicit
a="1"
print(type(a))
b="2"
print(type(b))
print("\n",int(a)+int(b))   #explicit coversion=conversion of data type from one into another done via programmer

#implicit

c=1.9
print(type(c))
d=8
print(type(d))
print(c+d)     #implicit conversion=conversion of data type from one into another done by python(from lower to higher)
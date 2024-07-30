a=12345
b="Frank" # " Frank" is a string . Frank will be treated as variable
c= True
d= None
print(a)
print(b)
c=744
print(a+c) #you can add same type of variable it would have given syntax error in case of a+b or b+c
print("The variable type of a is" , type(a))
print("The variable type of c is" , type(c))
print("The variable type of d is" , type(d))
print("The variable type of b is" , type(b)) # type() gives the type of variable
print("\n\n")

# NUMERIC DATA TYPE

# int=3,4,5
# float=3.001,0.0001
# complex=6+2i

# STRING DATA TYPE="Frank is a good boy"


list1=[8,2.3,[-4,5.0],["apple","bannana"]] 
 #ordered collection of data with elements separated by a comma and enclosed within Third bracket
print(list1)     
#lists are mutable and can be modified after creation



dict1={"name":"Frank","age":20,"Can Vote":True}
#unordered collection of data containing a key:value pair enclosed in Second Bracket
print("\n",dict1)



tuple1=("parrot","sparrow") , ("lion","tiger")
# ordered collection of data with elements separated by a comma and enclosed within First bracket
print("\n",tuple1)
#tuple are immutable and cannot be modified after creation


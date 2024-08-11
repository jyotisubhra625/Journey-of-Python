
def function():

 try:
     l=[1,5,6,7]
     i=int(input("Enter the index : "))
     print(l[i])
     return True

 except:
     print("Some error occured")
     return False

 finally:
     print("End of code")    #it is always executed

x=function()
print(x)
    
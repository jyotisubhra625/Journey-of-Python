def average(a,b,c=1):
    print("The average is ",(a+b+c)/3)
   
# average()     #gives error as the value of a and b are not defiened in the argument
# average(c=9)  
# # average(a=1)    #gives error as the value of b is not given in the argument
# average(b=20)   #gives error as the value of a is not given in the argument

average(a=3,b=2)
average(3,2)         #same as the upper line


def averages(*numbers):       #stores the number in the form of tuple
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is ",sum/len(numbers))   #len(numbers) gives the length of the tuple
averages(1,2,3,4,5,6,7,8,9)

def averages(*numbers):       
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
        # return 7     #it returns 7 upon calling the function
        #the first return is returned upon calling
        return sum/len(numbers) #returns the average upon calling 
    
#if return is not used it gives none
   
c=averages(1,2,3,4,5,6,7,8,9)
print(c)


def name(**name):
    print(type(name))
    print("Hello ",name["fname"],name["mname"],name["lname"])
    
name(mname="Kumar",fname="Rahul",lname="Sharma")   


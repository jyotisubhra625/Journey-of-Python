x=int(input("Enter the value of x: "))
match x:
    case 0 :
        print("x is zero")
    case 5 :
        print("x is five")
    case _ if (x==90):         
        print("x is 90 ",x)
    case _ if (x==80):         
        print("x is 80 ",x)
    case _ if (x==70): 
        print("x is 70")   
    case _:           #this is a default case
        print("x is neither zero nor five",x)


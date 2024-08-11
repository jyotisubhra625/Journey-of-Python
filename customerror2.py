a=input("Enter a number between 5 and 9 : ")
a.lower()
if(a=="quit"):
    print("Program exitted.")
elif(int(a)<5 or int(a)>9):
    raise ValueError("Number should be between 5 and 9.")
elif(int(a)>=5 and int(a)<=9):
    print(a)
else:
    raise ValueError("Invalid number")



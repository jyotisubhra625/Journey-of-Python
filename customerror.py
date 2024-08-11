a=int(input("Enter any value between 5 and 10"))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")  #raise custom errors using 'raise' keyword

print(a)
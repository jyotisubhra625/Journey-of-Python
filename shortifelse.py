a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
print("A",a) if a>b else print("=") if a==b else print("B",b)

print("1") if a>b else ""       #if you want to print only if a condition is satisfied use if and then use else "" otherwise it gives error



result="A is greater" if(a>b) else "B is greater"
print(result) 


'''result=value_if_true if condition else value_if_false'''


'''
if condition:
 result=value_if_true
else:
 result=value_if_false
'''
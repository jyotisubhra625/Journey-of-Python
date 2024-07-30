#for loops can iterate over a sequence of iterable objects

n=input("enter a string: ")
for i in n:
    print(i)  # prints each character in the string
    if(i=='b'):
        print("this is something special")

c=['red','green','yellow','blue']
for colour in c:
    print(colour)  # prints each item in the list
    for i in colour:
        print(i)  # prints each item in the list again

for k in range(5):
    print(k)  # prints numbers from 0 to 4
    print(k+1)# prints numbers from 0 to 5

for k in range(1,9):
    print(k)  # prints numbers from 1 to 8

for k in range(1,12,3):
    print(k)  # prints numbers from 1 to 9 with a step of 3



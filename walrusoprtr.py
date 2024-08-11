# a=True
# print(a:=False)


# numbers=[1,2,3,4,5]
# while(n :=len(numbers))>0:
#     print(numbers.pop())

'''Walrus operator :=

new to Python 3.8
assignment expression aka walrus operator
assigns values to variables as part of a larger expression'''

happy=False
print(happy)

print(happy:=True)

foods=list()

#AAM ZINDIGI

# while True:
#     food=input("Enter a food: ")
#     if food=="quit":
#         break
#     foods.append(food)
# print(foods)

#MENTOS ZINDAGI

while(food := input("Enter a food : ")) != "quit":
    foods.append(food)
print(foods)
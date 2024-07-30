marks=[60 , 40 , 80 , "Frank" , "Harry ", True ]    #lists are ordered collection of data items and are mutable
#      [0]  [1]  [2]    [3]       [4]      [5]
#lists are changeable meaning we can alter tham after creation
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
# print(marks[6])    #gives error as indexation starts from 0
print("Marks at -3 : ",marks[-3])     #negative index.To convert it into positive index (len(marks)-3)

if 7 in marks:
    print("7 is present in the list")
else:
    print("7 is not present in the list")

if "Frank" in marks :
    print("Frank is present in the list")
else:
    print("Frank is not present in the list")

if "rank" in "Frank":
    print("rank is present in the string")
else:
    print("rank is not present in the string")

print(marks[:])

print(marks[1:])

print(marks[1:4:2])
#prints every 2nd element
print(marks[2:len(marks)])


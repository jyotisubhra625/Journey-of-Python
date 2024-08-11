#MAP

# def cube(x):
#     return x*x*x

# print(cube(2))
l=[1,2,4,6,5,3]
# newl=[]
# for item in l:
#     newl.append(cube(item))



#map() applies a function to each element in a sequence and returns a new sequence

newl=list(map(lambda x: x*x*x,l))   #map(function,iterable)



#returns value as map
print(newl,type(newl))

#FILTER
def filter_function(x):
    return x > 3
newl2=list(filter(filter_function,l))      #filter(predicate(function),iterable)
#filter() filters a sequence of elements based on given predicate () 
print(newl2)
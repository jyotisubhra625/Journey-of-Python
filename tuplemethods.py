countries=("Spain","Italy","India","England","Germany")
print(countries)
temp=list(countries)    #converts the tuple into list as tuples are not mutable
#after converting the tuple into list it is stored in temp

temp.append("Russia")   #add item
temp.pop(3)             #remove item
temp[3]="Finland"       #change item

countries=tuple(temp)   #converts the list back to tuple
print(countries)

c2=("Pakistan","Afghanistan","Bangladesh","Sri lanka")
s=countries+c2         #concatenation
print(s)

t=(0,1,2,3,4,3,2,1,3,2,1)
r=t.count(3)          #counts the number of times a value is repeated
print(r)

p=t.index(3)
print(p)
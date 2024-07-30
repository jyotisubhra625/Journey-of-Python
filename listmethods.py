l=[1,28,23,14,50,96]
print(l)

print(l.index(28))        #gives the indexation of the value inside

l.append(7)               #add 7 at the end of the list
print(l)

l.sort()                  #sort the list in ascending order
print(l)
l.sort(reverse=True)      #sort the list in descending order
print(l)

l.reverse()               #reverses the list
print(l)

m=l.copy()                #used to copy contents of m into l
                          #using m=l is not a great idea as if you change the value of m the value of l will also change
m[0]=0
print(l)        

l.insert(1,899)           #inserts a value at the defined index (index,value)
print(l)

m=[900,1000,1100]   
k=l+m                    #concatenates two lists
print(k)
l.extend(m)              #adds the values of this list to the list given(concatenation)
print(l)

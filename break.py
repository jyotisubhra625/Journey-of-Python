#break statement enables a pogram to skip over a part of the code.it terminates the very loop it lies within
for i in range(1,12):
    if(i==10):
        break
    print("5 x ",i+1," = ",5*(i+1))
print("Got Out of the Loop! ") 

#continue statement skips the rest of the code inside a loop for the current iteration only
for i in range(1,12):    
    if(i==10):
        print("Skipped the iteration")    #here 10 gets skipped
        continue
    print("5 x ",i," = ",5*i)

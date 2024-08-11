#enumerate function allows you to loop over a sequence and get the index and value 
# of each element in the sequence at the same time
marks=[12,45,78,23,56,89,32,65,55]
for index,mark in enumerate(marks):
    print(mark)
    if(index==5):
        print("Frank,Awesome!")
        
        
fruits=["mango","apple","banana","pineapple","jackfruit"]
for index,fruit in enumerate(fruits):
    print(index,fruit)

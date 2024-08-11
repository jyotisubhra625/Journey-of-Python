import os
folders=os.listdir("Data")

#os.chdir("C:\Users\SUBHRAJYOTI\Desktop\New folder (2)")
print(folders,type(folders))

for folder in folders:
    print(folder)
    
for folder in folders:
    print(folder)
    print(os.listdir(f"Data/{folder}"))
    
print(os.getcwd())
    
    
    
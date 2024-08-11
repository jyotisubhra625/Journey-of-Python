import os


for i in range(0,100):
    #os.rename(f"Data/Day{i+1}",f"Data/Code{i+1}")   #the folder name is converted from Day to Code
    os.rename(f"Data/Code{i+1}",f"Data/Code {i+1}")
    
f=open('myfile2.txt','r')
i=0
while True:
    i+=1
    line = f.readline()
    if not line:
        # print(line,"\t",type(line))
        break
    m1=line.split(",")[0]    #dat type-string
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    
    print(f"Marks of student {i} in Mathematics is : {m1} ")
    print(f"Marks of student {i} in Social Studies is : {m2} ")
    print(f"Marks of student {i} in Science is : {m3} ")
    print(line)
    
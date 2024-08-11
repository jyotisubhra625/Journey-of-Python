'''
 read r
 write w
 append a
 create x
 text t
 binary b=used to handle binary files(images,pdfs,etc)
'''
#READING A FILE

#f=open('myfile.txt','r')
#print(f)
#text.f.read()
#f.close()



#WRITING A FILE

# f=open('myfile.txt','w')
# f.write('Hello World!')
# f.close()


#APPENDING IN A FILE

# f=open('myfile.txt','a')
# f.write(' Hello World! ')
# f.close()


with open('myfile.txt','a') as f:
    f.write("Hey I am inside with the help of Python")
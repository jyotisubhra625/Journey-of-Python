with open('file.txt','r') as f:
    # print(type(f))
    # Move to the 10th byte in the file
    
    f.seek(10)            # seek() allows you to move the current position within a file to  specific point inside ()
    
    
    
    
    print(f.tell())  # tell() returns the current position within the file in bytes
    
    
    
    # Read the next 5 bytes
    
    data=f.read(5)      # read() reads the number of characters written inside()
    print(data)
    
    
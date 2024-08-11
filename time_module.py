import time
# print(time.time())

# print("Start :",time.time())
# time.sleep(10)
# print("End : ",time.time())

# t=time.localtime()
# format_year=time.strftime("%d/%m/%Y")
# format_time=time.strftime("%H:%M:%S")
# print(format_year)
# print(format_time)

def usingWhile():
    i=0
    while i<=5000:
        i=i+1
        print(i)
def usingFor():
    for i in range(5000):
        print(i)
        
init=time.time()
usingFor()
t1=time.time()-init
init=time.time()
usingWhile()
t2=time.time()-init

print("For Loop in   : ",t1,"s")
print("While Loop in : ",t2,"s")
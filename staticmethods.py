class Math:
    def __init__(self, num):
        self.num=num
    def addtonum(self,n):
        self.num+=n
    @staticmethod   
    def add(a,b):
        return a+b
    
a=Math(5)
print(a.num) #5
(a.addtonum(6))
print(a.num)

print(a.add(7,9))
print(Math.add(7,9))


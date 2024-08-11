# def double(x):
#     return x*2
# print(double(5))
def appl(fx,value):
    # Applies the given function fx to the value and adds 6 to the result
    return fx(value)+6

double=lambda x: x*2
cube=lambda x: x*x*x
avg=lambda x,y,z:(x+y+z)/2 

print(double(5))
print(cube(5))
print(avg(2,3,5))
print(appl(cube,2))
 # Applies the cube function to 2 and adds 6, printing 14
 
print(appl(lambda x: x*x*x,2))  
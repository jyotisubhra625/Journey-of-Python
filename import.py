# import math
# print(math.sqrt(9))

# from math import sqrt,pi
# r=sqrt(9)*pi
# print(r)

from math import *  
'''imports all the functions and variable from a module (not recommended as it can lead to confusion 
and make it harder to understant where specific functions and variable are coming from)
'''
r=sqrt(9)*pi
print(r)

import math as m
from math import pi,sqrt as s

r=s(9)*pi
print(r) 
print(m.sqrt(9)*pi)


import math
print(dir(math))
print(math.sin,type(math.sin))

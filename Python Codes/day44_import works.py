# import math #--> we can use math functions after importing math
# print(math.sqrt(9)) #--> here the synrax is module.function()

# import math as math_function  #--> we can change module name using this
# print(math_function.sqrt(9))

# from math import sqrt,pi print #--> using from we can import specific functions and we can use function without '.'
# mul=sqrt(9)*pi
# print(mul)

# from math import *  #--> it import all function in math 
# mul=sqrt(9)*pi
# print(mul)

# import math
# print(dir(math)) #--> it will print all functions of math module
# print(math.nan,type(math.nan))

# ************************import from file*****************************	

# import test  #--> if use only import then use . operator and it will import test file from file manager 
# test.welcome()
# print(test.name)

# import test as t  #--> instead of test use t to access functions 
# t.welcome()
# print(t.name)

from test import welcome,name   #--> here no need to use . to access use only function 
welcome()
print(name)
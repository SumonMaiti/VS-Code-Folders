a=34  #--> global variable -- outside the function
print (f"The value of a in golbal is {a}")
def welcome():
	# global a #--> it will cahnge the a global variable now the global variable became 3 
	a=3   #--> local variable -- in the function 
	print(f"The value of a in function is {a}")
	b=00
print(f"before function calling a={a}")
welcome()
# print(b) #--> we can not access loacl variable outside the function

# ** if local variable exist inside function  then it take local otherwise it take  global variable 
# ** if we change local variable global variable remain constant
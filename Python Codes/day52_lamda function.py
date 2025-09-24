def cube(x):
	return x*x*x

print(cube(3))
# =================================================================
# to easier the upper program we use lambda funcion
# we can give function as argument in function using lambda
cube=lambda x:x*x*x

print(cube(3))

# Example:-->
def func(fx,argument):
	return fx(argument)
print(func(lambda x:x*x*x,3))


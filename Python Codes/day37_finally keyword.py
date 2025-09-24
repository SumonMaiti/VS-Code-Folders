# **main use of finally keyword is in function**
# try:
# 	index=input("Enter an index:")
# 	print(f"your index is {index}")
# 	l=[45,67,43,78,9]
# 	print(l[index])
# except:
# 	print("Some error occured!!")
# finally: #--> main use of finally keyword is in function
# 	print("i will always executed")


def func1():
	try:
		index=int(input("Enter an index:"))
		print(f"your index is {index}")
		l=[45,67,43,78,9]
		print(l[index])
		return 1
	except:
		print("Some error occured!!")
		return 0
	finally: #--> if the program return a value then this statement always execute
		print("i will always executed")

x=func1()
print(x)
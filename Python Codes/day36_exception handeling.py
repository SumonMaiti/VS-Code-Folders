# a=input("Enter a number: ")
# try:
# 	for i in range(1,11):
# 		print(f"{int(a)}X{i}={int(a)*i}")
# except Exception as e: 
# except:                               #--> if there is an error this will be terminated
# 	print("invalid input")
# print("Successfully terminated")
# simmilarly we can use🚙

# except ValueError:

# except IndexError:
try:
	num=int(input("Enter a number:"))
	a=[5,4,2]
	print(a[num])
except ValueError:  #--> we can use many error in a program
	print("There is an value error in your program")
except IndexError:  #--> if there is an index error this will be executed
	print("There is an index error in your program")
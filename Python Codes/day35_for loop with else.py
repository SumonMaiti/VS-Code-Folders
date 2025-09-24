for i in range(12):
	print(i)
	if(i==10):
		break #--> **if there is an break then the control will not go to else because for loop is not executed
		      #     completely. 
	
else: #--> if for statement executed successfully then else will execute  and it is same for while loop.
	print("the control is now in else statement")
print("successfully executed")
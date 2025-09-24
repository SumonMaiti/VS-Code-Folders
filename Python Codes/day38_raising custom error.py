s=input("Enter a number between 5 to 8:")
if (s =='quit'):
	print("You have quited the program")
elif( int(s)<=4 or int(s)>=9):
	raise ValueError("value should between 5 to 8") #--> if the condition is not true this will print
else:
	print("your input is ",s)
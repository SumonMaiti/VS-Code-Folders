import random
print("@@@@@@@@@@ weccome to Snake Water Gun game@@@@@@@@@@\n")
comp_choice=[-1,0,1,1,0,-1,-1,0,1,1,0,-1,1,0,1,-1,0,-1,0,1,1,0,-1,-1,0,1,1,0,-1,1,0,-1,-1]
n= random.choice(comp_choice)

user_choice=int(input("Enter -1 for Snake , 0 for Water and 1 for Gun :"))

if  n == -1:
	print("computer chose Snake as input")
	if user_choice==-1:
		print ("The game  is draw")
	elif user_choice==0:
		print ("You lost the game")
	elif user_choice==1:
		print ("You won the game")
	else:
		print("Please don't enter anything else")
elif n == 0:
	print("computer chose Water as input")
	if user_choice==0:
		print ("The game  is draw")
	elif user_choice==1:
		print ("You lost the game")
	elif user_choice==-1:
		print ("You won the game")
	else:
		print("Please don't enter anything else")
elif n == 1:
	print("computer chose Gun as input")
	if user_choice==1:
		print ("The game  is draw")
	elif user_choice==-1:
		print ("You lost the game")
	elif user_choice==0:
		print ("You won the game")
	else:
		print("Please don't enter anything else")
else:
	print("some error occured")

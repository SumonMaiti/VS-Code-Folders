import random
print("@@@@@@@@@@ welcome to Snake Water Gun game @@@@@@@@@@\n")
while True:
	comp_choice=(-1,0,1,1,0,-1,-1,0,1,1,0,-1,1,0,1,-1,0,-1,0,1,1,0,-1,-1,0,1,1,0,-1,1,0,-1,-1)
	n= random.choice(comp_choice)  #--> put the randon choice value into n variable for easy
	input_comp={-1:"Snake",0:"Water",1:"Gun"}   #--> creating dictionary for printing inputs
	user_choice=int(input("Enter -1 for Snake , 0 for Water ,  1 for Gun  or 3 to quite  :  "))  #--> take input from user
	try:
		print(f"You entered : {input_comp[user_choice]}")  #--> print inputs
		print("computer entered : ",input_comp[n])  #--> print inputs
		     #--> using try except because i am using dictionary and n==9,8.. is not defined it will through  an error
	except:                   
		if user_choice == 3:
			print("You quited the game")
			break
		print("please enter between -1,0,1,3 nothing else")
	if  (n == -1 and user_choice==-1) or  (n == 0 and user_choice==0) or  (n == 1 and user_choice==1):
		print ("The game  is draw  ＞﹏＜")
	elif (n == -1 and user_choice==1) or  (n == 0 and user_choice==-1) or  (n == 1 and user_choice==0):
		print("You won the game (●ˇ∀ˇ●)")
	elif (n == -1 and user_choice==0) or  (n == 0 and user_choice==1) or  (n == 1 and user_choice==-1):
		print("You lost the game !!!")
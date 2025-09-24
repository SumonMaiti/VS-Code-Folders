questions=[['what is your name?','1.Arnab','2.Sumon','3.Abhijit','4.Sumit'],
['what is your age?','1.23','2.45','3.76','4.18'],
['what is your father name?','1.Ashok','2.Adak','3.Kushal','4.Aman'],
['what is your mother name?','1.Kunti','2.Aparna','3.Priya','4.Ajay']]

for i in range(4):
	question=questions[i]
	print('Question no.',i+1,'-->',question[0])
	print("Your options are--------")
	# for j in range(1,5):
	# 	print(question[j])
	print(f"{question[1]}          {question[2]}")
	print(f"{question[3]}        {question[4]}")
	ans=int(input("Enter 1-4 as your answer or 0 to quite : "))  #--> convert string to intiger
	if i == 0:
		if ans == 2:
			print("correct answer!!")
		elif ans==0:
			print("You have quited the game")
			break
		else:
			print("wrong answer!!")
			break
	if i == 1:
		if ans == 4:
			print("correct answer!!")
		elif ans==0:
			print("You have quited the game")
			break
		else:
			print("wrong answer!!")
			break
	if i == 2:
		if ans == 1:
			print("correct answer!!")
		elif ans==0:
			print("You have quited the game")
			break
		else:
			print("wrong answer!!")
			break
	if i == 3:
		if ans == 2:
			print("correct answer!!")
		elif ans==0:
			print("You have quited the game")
			break
		else:
			print("wrong answer!!")
			break
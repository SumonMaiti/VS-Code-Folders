# marks=[45,65,75,89,43,7,5]
# index=0
# for mark in marks:
# 	print(mark)
# 	if index==3:
# 		print("it is the highest mark")
# 	index+=1
# ================================================================
#*** to easy the upper program we use enumerate function
# marks=[45,65,75,89,43,7,5]
# for index, mark in enumerate(marks) : #--> remember the syntax if we change syntax value will change
# 	print(mark)
# 	if index==3:
# 		print("it is the highest mark")



fruit=['apple','banana','mango']
for index, fruit in enumerate(fruit,start=1) : #--> thus we can start index from 1 using start 
	print(fruit)
	if index==1:
		print("upper fruit is banana")
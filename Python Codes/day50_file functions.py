# @@@@@@@@@@@ read line method @@@@@@@@@@

# f=open("abc.txt","r")
# # line=f.readline()
# # print(line) #--> if we do like that it will print only one line so , we will use loop 
# while True:
# 	line=f.readline() #--> it will read file line one by 
# 	if not line: #--> if no line present then break the loop
# 		break
# 	marks=line.split(",") #-->split line into list where , is present
# 	# print(type(marks)) #--> check type of marks variable
# 	mark1=marks[0]        #--> take mark from marks list
# 	mark2=marks[1]       #--> after typecasting we can do operation 
# 	mark3=marks[2]
# 	print(f"first mark is = {mark1}")
# 	print(f"second mark is = {mark2}")
# 	print(f"third mark is = {mark3}\n")
# f.close()

# @@@ we can store highest score in game using file @@
 
 # ====================================================================================================

# @@@@@@@@@ write line method @@@@@@@@@@

f=open("abc.txt","w")
lines=['line 1\n','line 2\n','line 3\n']  #--> remember to add \n to write next line
f.writelines(lines)                       #--> we can write lines using this
f.close()



	

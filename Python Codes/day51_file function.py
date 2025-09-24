# @@@@@@@@@@@@ count no. of line in a file @@@@@@@@@@@ 

# f=open("abc.txt","r")
# linecount=1
# while True:
# 	line=f.readline(1) #-->it will read only one character from file
# 	if line=="\n":
# 		linecount+=1
# 	if not line: #--> if no line present then break the loop
# 		break
# print(linecount)
# ======================================================================================
# with open("abc.txt","r") as f:
# 	print(type(f))
# 	f.seek(10)      #--> cursour will go to 10 character not index
# 	print(f.tell()) #--> find the position of cursour
# 	data=f.read(5)  #--> take only 5 characters
# 	print(data)
# ========================================================================================
with open("abc.txt","w") as f:
	f.write("Hi sumon")
	f.truncate(5) #--> only 5 character will there in file using this function other character wil delete

with open("abc.txt","r") as f:
	print(f.read())
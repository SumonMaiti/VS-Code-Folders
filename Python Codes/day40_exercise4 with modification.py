print(" *****************🤫🤫Welcome to private chat🤫🤫******************\n ")
import random   #--> use import module to use random functions in list
# des=int(input("if you want to coding press 1 if you want to decoding press 2 or press 0 to quit:"))
def code():
	# if des==1:
		nword=[]
		rand=["hui",'jki','ety','reo',"kli","hro","bnm","ewq","itr","qbc","nbq","moz","niq","rqw"]
		ch=input("Enter your message : ")
		encrypt=int(input("enter encryption number:"))

		words=ch.split(" ") #--> split message into list
		for word in words:
			if len(word)<3:
				newstr=word[::-1]	#--> reverse the word		
			else:
				newstr=random.choice(rand)+word[1:]+word[0]+random.choice(rand)#--> we can call random element from list
			nword.append(newstr) #--> append newstr  in nword
		print(" ".join(nword))#--> join all elements of nword using space
		return encrypt
def decode():
	# if des==2:
		nword=[]
		ch=input("Enter your secret code : ")
		words=ch.split(" ") #--> split message into list
		
		for word in words:
			if len(word)<3:
				newstr=word[::-1]	#--> reverse the word		
			else:
				newstr=word[-4]+word[3:-4]
			nword.append(newstr) #--> append newstr  in nword
		print(" ".join(nword))#--> join all elements of nword using space
		# ih bnmumonsrqw etyouynbq ewqreahro ewqellwmoz
encryp=code()
enccode=int(input("Enter your encryption number to decode:"))
if(enccode==encryp):
	decode()
else:
	print("sorry!! you can't decode because you entered different encryption number")
	goto 
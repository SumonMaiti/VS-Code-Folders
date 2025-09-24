# ************************day9******************
# b=8.9
# a=3
# print(a+b)

# @@@@@@@@@@@@@@ mathematical operators@@@@@@@@@@@@@

# Multiplication  --->  *  Ex.-> 3*2 = 6   
# Addition        --->  +  Ex.-> 3+2 = 5
# Subtraction     --->  -  Ex.-> 3-2 = 1
# Division        --->  /  Ex.-> 3/2 = 1.5
# Remainder       --->  %  Ex.-> 3%2 = 1
# Power           --->  **  Ex.-> 3**2 = 3X3=9 
# Floor Division  --->  //  Ex.-> 3//2 = 1
# ===============================***===================================================================
# ****************************day10*****************
# a=input("Enter 1st number :")
# b=input("Enter 2nd number :")
# print(a+b)
# print(int(a)+int(b))
# ================================***===================================================================
# *********************************day11***********
# name='sumon'
# lname='maiti'
# print('hello',"Mr.",name, lname)
# print("He said,\"I want to eat an apple\""'.')
# apple="""He said  , 
# "i   am, a student\""""""#------------>to use multiline sring use triple single or double quote
# print(apple)
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])#-------------> throw an error because 5 index does nor exist in name variable
# =====================================***==============================================================
# *****************************day12**************************
# m="mango"
# print (len(m))#--------->find length of a string using len() function
# print(m[0:5])
  	  #   | |_____>>it will print  index 0 to index 4(n-1)
	  #   |_____________>>start from 0 indrx position.if we don't write 0 it automatically initialize 0
# print(m[0:-2])
		 #   |_____>>it will automatically convert into len(m)-2
# print(m[1:4])
#         |_____>>from index 1 to index 3(n-1)
# print(m[-3:-1])
#             |_____>>it will be converted into m[len(m)-3:len(m)-2] --> [5-3 : 5-2] --> [2:3]
# print(m[-2:-3])
#             |_____>>it will be converted into m[len(m)-2:len(m)-3] --> [5-2 : 5-3] --> [3:2]-->it does not make any sense.
# =========================================***=============================================================
# ****************************Day13*********************************
# a="suMoN"
# print(len(a))
# b=a.upper() #--> this function will not change the value of a
# print(b)
# print(a)
# print(a.upper())#---->previous value of a will not change .it will convert whole string into upper case

# print(a.lower())#---->previous value of a will not change .it will convert whole string into lower case
# print(a)

# a="!!!SUmOn!!!!!"
# print(a.rstrip("!"))#--->it can strip exclamatory mark after string but it can't strip mark before string

# a="sumon !!!"
# print(a.replace("sumon","ashok"))#-->it will replace sumon into ashok.
				   # |__<<___|

# a="sumon anjan aparna"
# print(a.split())# -->it will split the string where the space has and convert into list data type.
# print(a.split(" "))#--> upper split and this split is same use

# heading='introduction to PYTHON'
# print(heading.capitalize())#-->it will convert first word's first  letter into capital and other letter into small.

# str1="welcome to the console"
# print(len(str1))

# str1="welcome to the console"
# print(str1)
# print(len(str1))
# print(str1.center(53))#--> convert length of the string into 53 and introduce space in the first but len of str1 is constant
# print(len(str1))

# a="sumon maiti sumon"
# print(a.count('sumon'))
# #                |___>>it will count how many times the string is present in the variable.

# a="gour!!!"
# print(a.endswith("!")) #--> return True or False
# print(a.endswith("!!"))#-->if the string ends with the written character it will return True otherwise it will return False

# a="He's name is john.He is a great man"
# print(a.find("g"))#--> it will return the index position where the written string found first time.
# 				    #|__>>if the written string not found it will return -1.
# print(a.index("g"))#--> it will return the index position where the written string found first time.
				     #|__>> if the written string not found it will through error.
# str="welcomPtotheconsole"
# print(str.isalnum())#-->if there is only A-Z or a-z or 0-9 in the string it will return true .
# 					#|__>>if there is other character(!,#,@,space) with A-Z or a-z or 0-9 in the string it will return false.
# print(str.isalpha())#-->if there is only A-Z or a-z in the string it will return true .
# 					#|__>>if there is other character(!,#,@,space) or number(0-9) with A-Z or a-z in the string it will return false.
# print(str.islower())#--> if all character is small return true otherwise return false

# print(str.isupper())#--> if all character is capital return true otherwise return false

# print(str.isprintable())#--> not printable character is '\n','\t'

# str1=" "
# print(str1.isspace())#--> if there is only space using spacebar or tab it will return true.

# str1="		"
# print(str1.isspace())

# str1="My Name Is Sumon Maiti "
# print(str1.istitle())#--> if first alphabet of each word is capital it will return true otherwise return false.

# str1="My Name Is Sumon Maiti "
# print(str1.swapcase())#--> it will swap capital letter to small and small to capital.

# str1="My name Is Sumon maiti "
# print(str1.title())#--> it will make title mean first letter of all word wil capital.

# a="Sumon maiti"
# b="Sumon maiti"
# c=a
# print(a==b)
# print(a is c)
# print(b == c)
# =========================================================================================================
# *****************************Day14*******************************
# **** if we don't use typecasting the input is consider as string*************

# a=int(input("Enter your age")) #--> type cast used
# print("your age is ",a)
# if a>18:  # ---> we can also use if statement without calibracis()
# 	print("You can drive")
# else:
# 	print("You cannot drive")

# num=int(input("Enter any number :"))
# if(num<0):
#  print("The number is nagative")
# elif(num==0):
# 	print("The number is zero")
# else:
# 	print("The number is positive")
# 	print("yay!!!!!!!!!!!")

# a=int(input("Emter a number : "))
# print("Your number is ",a)
# if a<0:
# 	print("number is negative")
# elif(a>0):
# 	if(a<=10):
# 		print("number is between 1-10")
# 	elif(a>10 and a<=20):
# 		print("number is between 11-20")

# i=int(input("Enter a number : "))
# if i%2==0 : print("the number is even")
# if not i%2==0: print("The number is odd") 

# @@@@@@@@@@@@@@@  short hand if else  @@@@@@@@@@@@@

i=int(input("Enter a number : "))
print("The number is even") if i%2==0 else print("The number is odd")
# ===================================================================================================
# ******************************Day 16**********************************
# match case statement simmilar to switch case ic c language
# a=int(input("Emter a number : "))
# match a :
# 	case 1 :
# 		print("The number is one")#--> no need to write break statement 
# 	case 2 if a==2:
# 		print("The number is two")
# 	case _ if a==4:   #--> we can use if condition in default or other  statement
# 		print("The number is",a)
# 	case _ if a==5:
# 		print("The number is five")
# ===================================================================================================
# *****************************Day 17**************************************
# *****************foor loops in PYTHON**********
# a="name"
# for i in a:  #--> print all elements of a using i
# 	print(i)

# for x in range(1,50,5): #--> print 1 to 49 difference is 5
# 	print("Episode ",x)
# ===================================================================================================
# ******************************Day 18*************************************
# i=1
# while (i<=10):
# 	if (i == 8 ):
# 		print("skip")
# 		i=i+1
# 		continue                  #--> it will skip the iteration and go to next iteration
# # 	print("5x",i,"=",5*i)  
# 	print(f"5 X {i} = {5*i}")
# 	i=i+1

# i=0
# while True:
# 	print(i)
# 	i=i+1
# 	if i==5:
# 		break            #--> it will jump and break the iteration
# ==================================================================================================
# *****************************Day 20*************************/*
# def gmean(a,b):#--> creat new function
# 	mean=(a+b)/2
# 	print(mean)

# def fact(a):
# 	fact=1
# 	while a>0 :
# 		fact=fact*a
# 		a=a-1
# 	return(fact)

# a=5
# b=10
# gmean(a,b)
# c=78
# m=98
# gmean(c,m)
# n=fact(5)
# print(n)
# ========================================================================================================
# *********************Day 21***************************
# def average(a=8,b=8):                        #--> 1.default argument 
# 	print("the average is=",(a+b)/2)
# average()

# def name(fname,mname="fuck",lname="you"):    #-->1.default argumet
# 	print("Hllo,",fname,mname,lname)
# n=input("Enter your name : ")
# name(n)

# def average(a=8,b=8):                      
# 	print("the average is=",(a+b)/2)
# average(b=10,a=6)   #--> 2.keyword argument   
                       # ---> no need to give argument orderwise
   
# def average(a,b=8):                  #--> here a is 3.required argument                      
# 	# print("the average is=",(a+b)/2)
# 	c=(a+b)/2
# 	return c  #--> we can use return statement in function

# c=average(6)    												
# print(c)

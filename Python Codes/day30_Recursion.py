# ****************** factorial *****************
# def factorial(n):#--> function defination
# 	if(n==0 or n== 1): #--> base case
# 		return 1
# 	else:
# 		return n*factorial(n-1) #--> recursive case
# fac=factorial(5) #--> function calling
# print(fac)
# ==============================================================
# ****************fibonacci series without recursion***************
n=int(input("Enter number of terms you want to print : "))
a=0
print(a)
b=1
print(b)
for i in range (1,n-1):
	temp=a+b
	print(temp)
	a=b
	b=temp
# ==================================================================
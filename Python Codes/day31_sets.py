# set is collection of well defined object
# sets are unchangeable
s={2,5,6,2}
print(s)
info={'carla',19,False,4,5,19} #--> they don't maintain order means they print randomly 
print(info)
harry={} #--> it is not a empty set it is an dictionary
print(type(harry))
harry=set()#--> it is an emprty set
print(type(harry))
for i in info:  #--> set will print randomly 
	print(i)
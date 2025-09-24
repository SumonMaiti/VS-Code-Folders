# *********tuple are unchangeable*********
tup=(3,6,7,8,45,34) 
# tup[2]=7  #--> we can not change tuple like list.
# print(tup)
# print(type(tup))
# print(tup[0])
# print(tup[1])
# print(tup[-2])
# print(tup[3])
# print(tup[4])

# if 6 in tup:
# 	print("yes present")

# print(tup[0:3])
# for i in range(6):
# 	print(tup[i])
                                    #--> other method are same as list
# tup.append(6)  #--> we can not add element in tuple

print(tup.index(7)) #--> print index of given element

# tup.sort()  #--> we can not use this function in tuple
# print(tup)

k=(5,6,745,0,243)
n=tup+k  #--> we can add two tupple in another variable 
print(n)
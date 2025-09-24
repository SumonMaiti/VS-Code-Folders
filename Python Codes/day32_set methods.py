# ***************we can get different values as output in set****************
# s1={1,2,3,3}
# s2={3,6,7}
# # print(s1.union(s2)) #--> print union of two sets
# s1.update(s2) #--> put the extra value of s2 in s1  
# print(s1,s2)

# cities1={'india','kolkata','mumbai','chennai','delhi'}
# cities2={'ladakh','kochi','kolkata',"delhi"}
# print(cities1.intersection(cities2))  #--> it will print intersection of two sets
# print(cities1,cities2)
# cities1.intersection_update(cities2)#--> it will update intersection value into cities1
# print(cities1,cities2)

# cities1={'india','kolkata','mumbai','chennai','delhi'}
# cities2={'ladakh','kochi','kolkata',"delhi"}
# #cities3=cities1.symmetric_difference(cities2)#-->it will print element which are not common in to sets
# # print(cities3)
# cities3=cities1.difference(cities2)#--> give cities1 element which are not in cities2
# print(cities3)

# cities1={'india','kolkata','mumbai','chennai'}
# cities2={'kolkata','ladakh'}
# print(cities1.issuperset(cities2))#--> cities 2 te ja acha sob jodi cities1 e thake tahola true 
# cities3={'india','kolkata'}
# print(cities1.issuperset(cities3))#--> cities 3 te ja acha sob jodi cities1 e thake tahola true 
# print(cities3.issubset(cities1)) #-->jodi cities3 ,cities1 er ongso hoi tahole true

# cities={'india','kolkata'}
# cities.add('delhi') #--> add item in a set
# print(cities)

# # cities.remove('india') #--> remove item in a set
# # print(cities)

# cities.discard('india') #-->if the element is not present in ser it will not throw error. it will skip
# print(cities)

cities={'india','kolkata','mumbai'}
item=cities.pop() #--> it will pop random element
print(cities)
print(item)

# del cities #--> delete  all set

cities.clear() #--> clear all element of a set but don't delete the whole set
print(cities)
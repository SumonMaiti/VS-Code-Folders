#*** convert tuple into list to do all list methods  operation in tuple 
country = ("india",5,"pakistan","america",5,"china","afganistan",5,67,45,34,45)
# print(country)
temp=list(country) #--> we can change in a tuple after converting it in list by type casting
# print(list)

# temp.append("england") #--> add item in a list
# print(temp)

# temp.pop(0)  #--> remove item give index position as argument to remove
# print(temp)

# temp[0]=6  #--> change element in list.
# print(temp)

country=tuple(temp)  #--> convert list into tuple 
# print(country)

# print('count of 45 is :',temp.count(45)) #--> count n0. of occourance

print('index of 5 is :',country.index(5)) #--> print the index where it find first time

# print('index of 5 is :',country.index(5,2,8)) --> slice index 2 to 8 then find element 5

print('length of tuple is :',len(country)) #--> calculate length of the tuple
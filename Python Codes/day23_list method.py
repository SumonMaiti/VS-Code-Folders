list=[2,34,5,6,6]
# print(list)
# list.append(8) #--> we can add new content in a list using this  function in the last

# list.pop(2)  #--> we can remove content in a list using this  function.
# print(list)

# list.sort()  #--> we can sort content in ascending order in a list using this  function

# list.sort(reverse=True)  #--> we can sort element in descending order  in a list using this  function

# list.reverse()  #--> we can reversr element  in a list using this  function

# print(list.index(6)) #--> it will print index position of a element in a list

# print(list.count(6)) #--> it will count frequency  of a element in a list

# m=list #--> *if we write like that and change in m variable same change will happen with list  variable

# m=list.copy() #--> *to avoide upper condition use copy() function
# m[0]=0
# print(list)
# print(m)

# list.insert(1,78)#--> it will add 78 in index 1.
# print(list)

# m=[45,54,67,86]
# list.extend(m) #--> it will add m list in list variable
# print(list)
# k=list+m #--> in this case two variable (list and m) remain same and element will will be marged in k variable
# print(k)
h="sumon maiti hope you are well"
# for word in h:
# 	print(type(word))
newword=[]
words=h.split(" ") #--> where it will get space in string it will split string into list
for word in words:
	# if len(word):
	strnew=word+'r'
	newword.append(strnew)#--> join strnew in newword
print(" ".join(newword)) #--> join list element using space
#** list is a collection of different or same data type.**

# marks=[49,56,76,"harry"] #--> list can store multiple variable in one list variable.
#   * list are changeable and we add different data type 
# print(marks)
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(type(marks))
# print(marks[-3])  # --> convert (len(marks)-3)= 4-3=1
# if '49' in marks:  #--> we can find element using this.
# 	print("yes")   #--> it will print no because 49 stored as a intiger not string
# else:               #--> same thing applicable for string.
# 	print("no")
# if 'ha' in 'harry':  #--> we can also find element in a string using this.
# 	print("yes")   #--> it will print yes because ha stored in harry
# else:
# 	print("no")
# hi='sumonmaitiisagoodboy'
# # print(hi)
# # print(hi[0:5])
# # print(hi[0:2])
# print(hi[0:20:2])
			#   |__>> it will print 2,4,6,8,10... indexes. it is known as jump index
# marks=[49,56,76,"harry",89,'sumon']
# print(marks)
# print(marks[0:5])#--> print index 0 to 4(5-1)
# print(marks[1:2])
# print(marks[1:6:2])
# print(len(marks))
# print(marks[:])  #--> it will consider as [0:len(marks)s]
# list=[i for i in range(5)]  #--> list comprehension
# print(list)
# list=[i*i for i in range(5)]  #--> list comprehension
# print(list)
# list=[i for i in range(5) if i%2==0]  #--> list comprehension
# print(list)



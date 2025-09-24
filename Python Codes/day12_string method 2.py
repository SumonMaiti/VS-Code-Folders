m="mango"
print (len(m))#--------->find length of a string using len() function
print(m[0:5])
#   	| |_____>>it will print  index 0 to index 4(n-1)
# 	    |_____________>>start from 0 indrx position.if we don't write 0 it automatically initialize 0
print(m[0:-2])
# 		   |_____>>it will automatically convert into len(m)-2
print(m[1:4])
#         |_____>>from index 1 to index 3(n-1)
print(m[-3:-1])
#           |_____>>it will be converted into m[len(m)-3:len(m)-2] --> [5-3 : 5-2] --> [2:3]
print(m[-2:-3])
#           |_____>>it will be converted into m[len(m)-2:len(m)-3] --> [5-2 : 5-3] --> [3:2]-->it does not make any sense.
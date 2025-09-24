# &&&&&&&&&& we can write and  read in same program opening the file write and read mode &&&&&&&

# f=open("abc.txt") #--> it will open as default mode read mode

# read mode('r'),write mode("w"),append mode("a") are same as c language

# f=open("abc.txt","r") #--> first argument is file name and second argument opening mode
# text = f.read() #--> read text from file
# print(text)

# f=open("abc.txt","w") #--> erase the previous content and write new content
# f.write("nothing is impossible")

# f=open("abc.txt","a") #--> don't erase the previous content and write new content
# f.write("nothing is impossible")
# f.close()

# @@@@@@@ short method to open and close file @@@@@

with open("abc.txt","a") as f:
	f.write(" \nHey welcome to my program")
# --> no need to use fclose() function

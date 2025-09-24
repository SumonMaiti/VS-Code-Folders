# *************** we can creater own search module **************
import os
# if( not os.path.exists("data")): #--> check if there is data folder in directory
# 	os.mkdir("data") #--> create a foldar in this directory

# for day in range(100):
# 	os.mkdir(f"data/Day {day+1}") #--> create Day 1 to 100 folder in data
# 	for i in range(100):
# 		os.mkdir(f"data/Day {day+1}/form {i+1}") #--> create form 1 to 100  folder in every Day folder

# folders = os.listdir("data") #--> create a list of all folders in data folder
# print(folders) 

# for folder in folders: #--> print all folder in data folder
# 	print(folder)

folders = os.listdir("data") #list folders=["Day1","Day2","Day3","Day4","Day5","Day6"...... ]
for folder in folders: #--> print all folder in data folder  // folder ='Day1', folder ='Day2',folder ='Day3'.....
	print(os.listdir(f"data/{folder}")) #--> print list of file in folder docoment
# here it will print ["form 1","form 2","form 3","form 4","form 5","form 6","form 7","form 8"...........]

# print(os.getcwd()) #--> find directory

# os.chdir("O:/Code on Sublime Text") #--> change directory using this function
# print(os.getcwd())
# dic = {"tree":"green object",'leg':"two human organ"}
# print(dic["leg"])

# dic = {34:"neha",45:"sumon",76:"harry"}
# print(dic[34])  #--> syntax to access elements in dictionary

       # |-->key |-->value
info={"name":"sumon","age":34,"eligible":True}
# print(info['name'])     #--> print name in element if not present through error
# print(info.get("name")) #--> print name in element if not present print none
# print(info.keys())  #--> get all element in a dictionary
# print(info.values())  #--> get all values in a dictionary

# for key in info.keys():  #--> get all element in a dictionary
# 	print(info[key])

print(info.items()) #--> give key value pairs
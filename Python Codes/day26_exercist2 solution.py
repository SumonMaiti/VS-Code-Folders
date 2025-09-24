name=input('Enter your name : ')
import time #--> we can import time from device using this 
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))
# print(timestamp)
# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)
if hour>=0 and hour<12:
	print("Good morning ",name)
elif hour>=12 and hour<16:
	print("Good afternoon ",name)
elif hour>=16 and hour<20:
	print("Good evening ",name)
elif hour>=20 and hour<=24:
	print("Good night ",name)
name="sumon maiti"
def welcome():
	print("hello welcome to my code")

print(__name__) #--> if the file is executing from this location then print __main__ else print the file name where it is
if __name__ == "__main__":
	welcome()
	print("no boddy")
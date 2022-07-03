# Assignment 2_6   Star Reverse triangle pattern

def RevStarPattern(value):
	i=0;
	j=0;
	for i in range(value):
		for j in range(value):
			print("*",end=" ")
		value = value - 1
		print(" ")

def main ():

	count=int(input("Enter count for Reverse * Pattern : ")) 
	RevStarPattern(count)
	
if __name__=="__main__":
	main();		
# Assignment 2_2   Star Rectangle pattern

def StarPatt(value):
	i=0;
	j=0;
	for i in range(value):
		for j in range(value):
			print("*",end=" ")
		print(" ")

def main ():

	count=int(input("Enter the count you want for pattern : ")) 
	StarPatt(count)
	
if __name__=="__main__":
	main();			
# Assignment 2_8   Triangle pattern Number

def TriNumPattern(value):
	i=0;
	j=0;
	for i in range(value):
		for j in range(i+1):
			print(j+1,end=" ")
		value = value +1 
		print()
	
def main():

	count=int(input("Enter count for Triangle Number Pattern : ")) 
	TriNumPattern(count)
	
if __name__=="__main__":
	main();		
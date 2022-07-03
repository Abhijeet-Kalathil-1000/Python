# Assignment 2_7   Rectangle pattern Number

def RectNumPattern(value):
	i=0;
	j=0;
	for i in range(value):
		for j in range(value):
			print(j+1,end=" ")
		print()
	
def main ():

	count=int(input("Enter count for Reactangle Number Pattern : ")) 
	RectNumPattern(count)
	
if __name__=="__main__":
	main();		
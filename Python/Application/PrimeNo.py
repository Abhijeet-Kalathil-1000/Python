# Assignment 2_5	Prime number

def PrimeNum(value):
	count =0;
	if (value >1):
		for i in range(2,value):
			if(value % i) == 0:
				count = count+1
	if (count > 1):
		print("Not a Prime Number")
	else:
		print("Prime Number")

def main ():
	num=int(input("Enter a number to check if Prime : "))
	PrimeNum(num)
	
if __name__=="__main__":
	main();		
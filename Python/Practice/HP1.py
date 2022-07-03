
def multi (value1,value2):
	ans = value1*value2
	return ans

def main ():
	
	print ("Welcome to Multiplication Programing")
	
	no1 = int(input("Enter 1st number : "))
	no2 = int(input("Enter 2nd number : "))
	
	ret = multi(no1,no2);
	
	print ("Multiplication is : ",ret)
	
if __name__ == "__main__":
	main();
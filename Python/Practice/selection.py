def maximum(value1,value2):
	if (value1>value2):
		return value1
	else :
		return value2

def main():
	
	no1=int(input("Enter 1st number : "))
	no2=int(input("Enter 2nd number : "))
	
	ret=maximum(no1,no2)
	print("Maximum no is ",ret);
	
if __name__=="__main__":
	main();
def Arithematic(value1,value2):
	add = value1 + value2
	sub = value1 - value2
	return add,sub

def main():
	no1=int(input("Enter 1st Number : "))
	no2=int(input("Enter 2nd Number : "))

	ret1, ret2 =Arithematic(no1,no2);
	
	print("Addition is : ",ret1)
	print("Substraction is : ",ret2)
	
if __name__=="__main__":
	main();
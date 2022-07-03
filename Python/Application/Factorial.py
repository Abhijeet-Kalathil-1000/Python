# Assignment 2_3		Factorial

def Fact(value):
	ans=1
	i=0;
	for i in range(value):
		ans = value*ans
		value =value-1
	return ans

def main ():
	count=int(input("Enter the number for factorial : ")) 
	ret=Fact(count)
	print(ret)
	
if __name__=="__main__":
	main();		
# Procedural approache

def add (value1,value2):
	ans=0
	ans=value1 + value2
	return ans
	
def main ():
	no1=0
	no2=0
	ret=0 
	
	no1=int(input("Enter no 1: "))
	no2=int(input("Enter no 2: "))

	ret=add(no1,no2)
	
	print("Addition is : ",ret)
	
if __name__=="__main__" :
	main ();
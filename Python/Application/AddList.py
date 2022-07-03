# Assignment 3_1 	Addlist

def AddList(value):
	sum =0
	for i in range(len(value)):
		sum =sum + value[i]
		
	return sum
	
def main ():
	count=int(input("Enter no of elemnts you want : "))
	Data = []
	
	print("Enter Elements : ")
	for i in range (count):
		Data.append(int(input()))
	print("Entered List is :",Data)
	ret=AddList(Data)
	print("Addition of List is :",ret)
	
if __name__=="__main__":
	main();		
#Addition of n number of data

import Marv

def main():
	count = int(input("How many elements you want ? "))
	
	Data = []
	print("Enter elements :")
	
	for i in range(count):
		Data.append(int(input()))

	print("Entered data : ",Data)
	
	ret = Marv.AddNum(Data)
	
	print("Addition of the list is : ",ret)
if __name__=="__main__":
	main();
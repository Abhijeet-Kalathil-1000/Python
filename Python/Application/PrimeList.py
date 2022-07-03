# Assignment 3_1 	Addlist Prime only

import Marvellous

def AddList(value):
	sum =0
	for i in range(len(value)):
		sum =sum + value[i]
		
	return sum
	
def main ():
    count=int(input("Enter no of elemnts you want : "))
    Data = []
    ret=[]
    element=int(input("Enter Elements : "))
    for i in range (count):
        print("in main for")
        ret=Marvellous.ChkPrime(element)
    print("Return ",ret)

	
    #ret2=AddList(Data)
    #print("Addition of List is :",ret2)
	
if __name__=="__main__":
	main();		
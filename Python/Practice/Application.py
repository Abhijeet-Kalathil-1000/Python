#import Marvellous
#from Marvellous import*
import Marvellous as M
import Infosystems

def main():
	print("Inside Moudule :",__name__)
	no1=int(input("Enter 1st Number : "))
	no2=int(input("Enter 2nd Number : "))

	ret1 = M.Addition(no1,no2);
	print("Addition is : ",ret1)
	
	ret2 = Infosystems.Substraction(no1,no2);
	print("Substraction is : ",ret2)
	
if __name__=="__main__":
	main();
# Assignment 1_2.2  Main Artithmetic

import Assignment2_1_1

def main():
	print("Enter two numbers : ")
	no1=int((input("First number : ")))
	no2=int((input("Second number : ")))
	
	ret=0
	print("\tWhich atritmentic operation do you want to perform ? :")
	type=int(input("Select from the below : \n\t 1) Addition \n\t 2) Substraction \n\t 3) Multiplication \n\t 4) Division\n"))
		
	if (type==1):
		ret=Assignment2_1_1.Add(no1,no2)
		print("Addition is ",ret)
		
	elif (type==2):
		ret=Assignment2_1_1.Sub(no1,no2)
		print("Substraction is ",ret)
		
	elif (type==3):
		ret=Assignment2_1_1.Mult(no1,no2)
		print("Multiplication is ",ret)
		
	elif (type==4):
		ret=Assignment2_1_1.Div(no1,no2)
		print("Division is ",ret)
		
	else:
		print("\t Wrong Selection ! ! ! !");

if __name__=="__main__":
	main();
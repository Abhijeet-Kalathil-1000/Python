# Assignment 2_1.1  #Module Arithmetic

def Add(value1,value2):
	ans =0
	ans = value1 + value2
	return ans
	
def Sub(value1,value2):
	ans =0
	ans = value1 - value2
	return ans
	
def Mult(value1,value2):
	ans =0
	ans = value1 * value2
	return ans
	
def Div(value1,value2):
	ans =0
	if (value2==0):
		print("Error ! Values not divisible by 0 ")
	else:
		ans = value1 / value2
		return ans
	
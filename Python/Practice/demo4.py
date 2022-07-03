
def fun():  #Function defination
	print ("Inside Demo 4");

def main():	
	print ("Inside main");
	fun();    #Function call
	
if __name__=="__main__":
	print(__name__)
	main();
	print ("End");
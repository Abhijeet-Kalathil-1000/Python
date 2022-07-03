
from sys import *

def main():
    print("__________________Marvellour Infosystem : Automation 1 __________________")
    print("script name : ",argv[0])
    print("Number of argument accepted : ",len(argv)-1)

    if len(argv) > 3 or len(argv) < 2:
        print("Invalid number of arguments")
        exit()

    if (argv[1] =='-u') or (argv[1] =='-U'):
        print("Usage : Script is used to perform additon of 2 numbers ")
        exit()
    
    if (argv[1] =='-h') or (argv[1] =='-H'):
        print("Help : Name_of_Script First_Argument Second_Argument")
        exit()

if __name__=="__main__":
    main()
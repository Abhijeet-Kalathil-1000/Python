
from sys import *

def Additon(iNo1,iNo2):
    ans = 0 
    ans = iNo1 + iNo2
    return ans

def main():
    print("__________________Marvellour Infosystem : Automation 1 __________________")
    print("script name : ",argv[0])
    print("Number of argument accepted : ",len(argv)-1)

    if len(argv) > 3 or len(argv) < 2:
        print("Invalid number of arguments")
        print("Use -u flag for udage information")
        print("Use -h for help ")
        exit()

    if (argv[1] =='-u') or (argv[1] =='-U'):
        print("Usage : Script is used to perform additon of 2 numbers ")
        exit()
    
    if (argv[1] =='-h') or (argv[1] =='-H'):
        print("Help : Name_of_Script First_Argument Second_Argument")
        exit()
    
    try:
        iRet= Additon(int(argv[1]) ,int(argv[2]))
        print("Addiotn is : ",iRet)

    except Exception:
        print("Exception while execution")
        print("Use -u flag for usage information")
        print("Use -h for help")
        print("Incase any issue with input check with Developer")

if __name__=="__main__":
    main()
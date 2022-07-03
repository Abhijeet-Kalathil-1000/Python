#Send email with attachemnt
from sys import *

from Attachemail import *
                
def main():
    print("__________________ Automation Send email with attachemnt __________________")
    #print("Directory name : ",argv[1])
    
    if len(argv) > 3 or len(argv) < 2:
        print("Invalid number of arguments")
        print("Use -u flag for udage information")
        print("Use -h for help ")
        exit()

    if (argv[1] =='-u') or (argv[1] =='-U'):
        print("Usage : Script is used to search particular extension files from a directory ")
        exit()
    
    if (argv[1] =='-h') or (argv[1] =='-H'):
        print("Help : Name_of_Script First_Argument(To) Second_Argument(file_name)")
        exit()
        
    try:
        Emailattach(argv[1],argv[2])

    except Exception:
        print("Exception while execution")
        print("Use -u flag for usage information")
        print("Use -h for help")
        print("Incase any issue with input check with Developer")

if __name__=="__main__":
    main()
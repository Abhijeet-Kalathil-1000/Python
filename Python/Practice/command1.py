from sys import *

def main():
    sum = 0 
    print("Number of cmmand line arg are :",len(argv))
    print("Name of application is : ",argv[0])

    print("Command line arguments are : ")
    for data in argv:
        print(data)
    sum = int(argv[1]) + int(argv[2])

    print("addition is  : ",sum)
if __name__=="__main__":
    main()

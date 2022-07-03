#Assignment 9_2
import os 

def FileRead():
    name = input("Enter the file name you want to display : ")

    if os.path.exists(name):
        fd = open(name,"r")
        data = fd.read()
        
        print("The data from the file is :\n",data)
        fd.close()

    else:
        print("No file found")

def main ():
    FileRead()

if __name__=="__main__":
    main()
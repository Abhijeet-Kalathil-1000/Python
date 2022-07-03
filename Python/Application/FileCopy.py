#Assignment 9_2
import os

def FileCopy():
    name = input("Enter the file name you want to copy : ")
    if os.path.exists(name):
        fd = open(name,"r")
        data = fd.read()
        print("Data is : ",data)

        name2 = input("Enter the new file name you want : ")
        fc = open(name2,"x")
        fc.write(data)
        fc.close()

    else:
        print("No Data Found")

def main():
    FileCopy()

if __name__=="__main__":
    main()
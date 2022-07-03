#Assignment 9_4
import os

def FileCompare():
    name1 = input("Enter the first file name you want to compare : ")
    if os.path.exists(name1):
        fd = open(name1,"r")
        data1 = fd.read()
    else :
        print("No File Found")
    
    name2 = input("Enter the second file name you want to compare : ")
    if os.path.exists(name2):
        fd = open(name2,"r")
        data2 = fd.read()
    else :
        print("No File Found")
    try:
        if data1 == data2:
            print("Successfull")
        else:
            print("Fail")
    except Exception:
        print("Unbound Local Error")

    
def main():
    FileCompare()

if __name__=="__main__":
    main()
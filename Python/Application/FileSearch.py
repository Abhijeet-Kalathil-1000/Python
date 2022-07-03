#Assignment 9_1
import os 

def FileSearch():
    name = input("Enter file name you weat to search : ")

    if os.path.exists(name):
        print("File exsts ")
    
    else:
        print("File doesn't exisits")

def main():
    FileSearch()

if __name__=="__main__":
    main()
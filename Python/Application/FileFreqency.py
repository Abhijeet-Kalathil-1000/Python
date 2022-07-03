#Assignemnt 9_5

import os

def FileFreq():
    name = input("Enter the file name you want to seach : ")
    word = input("Enter the word you want to search : ")

    if os.path.exists(name):
        fd = open(name,"r")
        data = fd.read()
        
        count = 0 
        for word in data():
            count = count + 1
        
        print("count of word is ",count)
        fd.close()
    else :
        print("No File Found")

def main():
    FileFreq()

if __name__=="__main__":
    main()
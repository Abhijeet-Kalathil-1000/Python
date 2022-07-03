#Assingment 8_4

import string
import threading


def SamllCase(a):
    low = []
    for i in range(len(a)):
        if i == str.islower(a):
            print("Lower case chars are : ",low)


def main():
    Data = input("Enter a string : ")
    thread1 = threading.Thread(target = SamllCase,args = (Data,),name="Small")
    thread1.start()

if __name__=="__main__":
    main()
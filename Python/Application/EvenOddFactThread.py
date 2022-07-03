#Assignment 8_2

import threading

def EvenFactor(no):
    Data= []
    for i in range (2,no+1):
        if no % i == 0:
            if i % 2 ==0 :
                Data.append(i)
    print("Even factors are : ",Data)
    print("Sum of Even factor is : ",sum(Data))

def OddFactor(no):
    Data =[]
    for i in range (2,no+1):
        if no % i == 0:
            if i % 2 !=0 :
                Data.append(i)
    print("Odd factors are : ",Data)
    print("Sum of Odd factor is : ",sum(Data))

def main():

    no = int(input("Enter a number to check factors : "))
    
    thread1 = threading.Thread(target = EvenFactor,args = (no,), name = "Even Factors")
    thread2 = threading.Thread(target = OddFactor,args = (no,), name = "Odd Factors")    

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exit from Main")

if __name__=="__main__":
    main()
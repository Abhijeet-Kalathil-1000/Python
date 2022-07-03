#Assingment 8_3

import threading

def EvenList(x):
    Elist = []
    for i in x:
        if i > 1:
            if i % 2 == 0:
                Elist.append(i)
    print("Even list is : ",Elist)
    print("Sum of Even list is : ",sum(Elist))

def OddList(a):
    Olist = []
    for i in a:
        if i % 2 != 0:
            Olist.append(i)
    print("Odd list is : ",Olist)
    print("Sum of Odd list : ",sum(Olist))

def main():
    Data = []
    count = int(input("Enter the size of list : ")) 
    for i in range(count):
        Data.append(int(input()))
    
    print("Entered list is : ",Data)
    
    thread1 = threading.Thread(target = EvenList,args = (Data,), name = "Even List")
    thread2 = threading.Thread(target = OddList,args = (Data,), name = "Odd List")    

    thread1.start()
    thread2.start()

if __name__=="__main__":
    main()
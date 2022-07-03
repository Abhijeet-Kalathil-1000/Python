#Assignment8_5
import threading
def Digits():
    for i in range(1,51):
        print(i,end=" ")
    print("\n")

def RevDigits():
    a = 51
    for i in range(50):
        a = a - 1
        print(a,end=" ")

def main ():
    
    thread1 = threading.Thread( target = Digits , args =(), name = ("Thread 1")) 
    thread2 = threading.Thread( target = RevDigits , args =(), name = ("Thread 2")) 

    thread1.start()
    thread1.join()
    
    thread2.start()
    thread2.join()

if __name__=="__main__":
    main()
# Assignemnt 8_1
import threading

def funEven():
    print("Thread name : ",threading.current_thread().name)
    for i in range(1,21):
        if i % 2 == 0:
            print(i ,end=" ")
            
def funOdd():
    print("\nThread name : ",threading.current_thread().name)
    for i in range(1,20):
        if i % 2 != 0:
            print(i ,end=" ")

def main():
    thread1 = threading.Thread(target = funEven,args = (),name = "Even")
    thread2 = threading.Thread(target = funOdd,args = (),name = "Odd" )

    thread1.start()
    thread2.start()

if __name__=="__main__":
    main()

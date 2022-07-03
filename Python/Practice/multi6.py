import os
import threading 

def Fun(X):
    print("Pid of fun : ",os.getpid())
    print("Parent Pid of fun : ",os.getppid())
    print("thread name Fun : ",threading.current_thread().name)
    print("Inside Fun ")
    for i in range(X):
        print("Fun : ",i)

def Gun(X):
    print("Pid of Gun : ",os.getpid())
    print("Parent Pid of Gun : ",os.getppid())
    print("thread name Gun : ",threading.current_thread().name)
    print("Inside Gun ")
    for i in range(X):
        print("Gun : ",i)

def main():
    No = 5 
    print("Pid of main : ",os.getpid())
    print("thread name of main : ",threading.current_thread().name)
    thread1 = threading.Thread(target = Fun,args = (No,),name = "FunThread")
    thread2 = threading.Thread(target = Gun,args = (No,),name = "GunThread")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    
    print("end of main")

if __name__=="__main__":
    main()
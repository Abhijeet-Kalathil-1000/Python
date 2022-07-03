import os
import multiprocessing 

def Fun(X):
    print("Pid of fun : ",os.getpid())
    print("Parent Pid of fun : ",os.getppid())
    print("Inside Fun ")
    for i in range(X):
        print("Fun : ",i)

def Gun(X):
    print("Pid of Gun : ",os.getpid())
    print("Parent Pid of Gun : ",os.getppid())
    print("Inside Gun ")
    for i in range(X):
        print("Gun : ",i)

def main():
    No = 5 
    print("Pid of main : ",os.getpid())
    process1 = multiprocessing.Process(target = Fun,args = (No,))
    process2 = multiprocessing.Process(target = Fun,args = (No,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    
    print("end of main")

if __name__=="__main__":
    main()
import os
import multiprocessing 

def Fun(X):
    print("Pid of fun : ",os.getpid())
    print("Inside Fun ")
    for i in range(X):
        print("Fun : ",i)

def Gun(X):
    print("Pid of Gun : ",os.getpid())
    print("Inside Gun ")
    for i in range(X):
        print("Gun : ",i)

def main():
    print("Pid of main : ",os.getpid())
    Fun(5)
    Gun(10)

if __name__=="__main__":
    main()
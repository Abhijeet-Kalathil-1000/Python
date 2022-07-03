import os 

def main():
    print("Hi")
    print("Pid of current process : ",os.getpid())
    print("Pid of parent process : ",os.getppid())

if __name__=="__main__":
    main()
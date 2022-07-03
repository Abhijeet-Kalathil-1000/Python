import os

def Fun():
    print("Pid of fun : ",os.getpid())
    print("Inside Fun ")
    for i in range(5):
        print("Fun : ",i)

def Gun():
    print("Pid of Gun : ",os.getpid())
    print("Inside Gun ")
    for i in range(5):
        print("Gun : ",i)

def main():
    print("Pid of maain : ",os.getpid())
    Fun()
    Gun()

if __name__=="__main__":
    main()
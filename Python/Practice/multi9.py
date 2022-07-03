import os
import multiprocessing


def Square(No):
    print("PID ",os.getppid())
    return No*No

def main():
    data = [5,3,35,64,5,51,4,8,2]
    p = multiprocessing.Pool()

    result =[]
    result = p.map(Square,data)

    print(result)

if __name__=="__main__":
    main()
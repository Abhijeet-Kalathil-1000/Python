import time
import multiprocessing
import os

def CheckEvenOdd(x):
    if x == 0:
        return 'zero'
    elif x % 2 == 0:
        return 'even'
    else:
        return 'odd'

def multiprocessing_func(x):
    time.sleep(4)
    print('PPID is {} PID is {} Input : {} results {}'.format(os.getppid(),os.getpid(),x, CheckEvenOdd(x)))

if __name__ == '__main__':
    
    print("Mult processed application : ")
    starttime = time.time()
    processes = []
    for i in range(0, 10):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
    endtime = time.time() 
    gap = endtime - starttime
    print('That took {} seconds'.format(gap))
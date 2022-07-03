import os
import multiprocessing

def main():
    print("No of core : ",multiprocessing.cpu_count())

if __name__=="__main__":
    main()
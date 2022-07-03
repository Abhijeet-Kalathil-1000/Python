#Assignment Automation 12_1 Process Information
import os
from sys import *
import multiprocessing
import getpass
import sys

def ProcessLog(X):
    username = getpass.getuser()
    name = multiprocessing.current_process().name
    sys.stdout = open("Demo/Log.txt","w")
    print("Process name is : ",name)
    print("Pid is : ",os.getpid())
    print("Username is : ",username)
    sys.stdout.close()

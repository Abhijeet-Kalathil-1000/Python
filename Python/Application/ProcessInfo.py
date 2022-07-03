#Assignment Automation 12_1 Process Information
import os
from sys import *
import multiprocessing
import getpass

def FunTest(X):
    username = getpass.getuser()
    name = multiprocessing.current_process().name
    print("Process name is : ",name)
    print("Pid is : ",os.getpid())
    print("Username is : ",username)


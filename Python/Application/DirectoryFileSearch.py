#Assignemnt 10_1
from sys import *
import sys
import os

def DirFileSearch(No1,No2):
    sys.stdout = open("Demo/Log1.txt","w")
    for root, dirs, files in os.walk(No1):
        for file in files:
            if file.endswith(No2):
                print(os.path.join(root, file))
    print("Output added from Automation : Directory File Search ")
    sys.stdout.close()
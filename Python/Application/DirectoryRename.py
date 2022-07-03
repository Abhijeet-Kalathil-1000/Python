#Assignemnt 10_2
from sys import *
import sys
import os

def DirRename(No1,No2,No3):
    folder = No1
    for filename in os.listdir(folder):
        infilename = os.path.join(folder,filename)
        if not os.path.isfile(infilename): continue
        oldbase = os.path.splitext(filename)
        newname = infilename.replace(No2,No3)
        output = os.rename(infilename, newname)
        print("Changes made for ",infilename)

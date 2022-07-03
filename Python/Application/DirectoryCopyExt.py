#Assignemnt 10_4
from sys import *
import sys
import os
from pathlib import Path
import shutil

def DirCopyExt(No1,No2,No3):
    if os.path.exists(No2):
       print("Directory already exists")
       files=os.listdir(No1)
       for fname in files:
           if fname.endswith(No3):
               shutil.copy2(os.path.join(No1,fname), No2)
       print("Files now coped")
    else:
        os.mkdir(No2)
        print("Created new dir '%s' is created " % No2)
        files=os.listdir(No1)
        for fname in files:
            if fname.endswith(No3):
                shutil.copy2(os.path.join(No1,fname), No2)
        print("Files copied to New Diretory")
    
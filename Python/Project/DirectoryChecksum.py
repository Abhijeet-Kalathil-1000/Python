#Assignment 11_1
from sys import *
import hashlib
import os

def hashfile(path, blocksize=1024):
    afile = open(path,"rb")
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0 :
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DirCheckSum(No1):
    Mydict = dict()
    for root, dirs, files in os.walk(No1):
        for file in files:
            Mydict[file] = hashfile(os.path.join(No1, file))

    with open(os.path.join(No1, "log.txt"), "w") as afile:
        for key, value in Mydict.items():
            afile.write("{} : {}\n".format(value, key))
            print("{} : {}".format(value, key))
        

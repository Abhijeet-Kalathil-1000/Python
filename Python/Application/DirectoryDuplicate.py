#Assignment 11_1
from genericpath import exists
from sys import *
import hashlib
import os
import time

def hashfile(path, blocksize=1024):
    afile = open(path,"rb")
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    
    while len(buf) > 0 :
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    
    return hasher.hexdigest()

def DirDuplicate(path):

    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    dups = {}

    if exists:
        for dirName,Subdirs,fileList in os.walk(path):
            #print("Current folder is :"+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid Path")     

def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))         

    if len(results) > 0:
        print("Duplicates Found:")
        print("The fllowing files are duplicate")
        for result in results:
            for subresult in result:
                print("\t%s"%subresult)
    else:
        print("No Duplicares fiels found")
#Assignment Automation 12_1 Process Information
import os
from sys import *
import psutil as ps 

def RunningProcess(No1):

    for proc in ps.process_iter():
        try:
            if No1.lower() in proc.name().lower():
                return True
        except (ps.NoSuchProcess, ps.AccessDenied, ps.ZombieProcess):
            pass
    return False



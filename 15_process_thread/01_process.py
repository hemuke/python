#! /root/anaconda3/bin/python
import time
import os
import multiprocessing

print(multiprocessing.current_process().pid)

print(os.getpid())

print(os.getppid())

time.sleep(1180) 

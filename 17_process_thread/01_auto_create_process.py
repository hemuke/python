#! /root/anaconda3/bin/python
import time
import os
from multiprocessing import current_process

print(current_process().pid)

print(os.getpid())

print(os.getppid())

time.sleep(200)

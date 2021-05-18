import os
os.makedirs('dirnames2/dirnames1')
os.removedirs('dirnames2/dirnames1')
open('abc.txt', mode="w")
os.remove('abc.txt')
open('oldname', mode="w")
os.rename('oldname', 'newname')

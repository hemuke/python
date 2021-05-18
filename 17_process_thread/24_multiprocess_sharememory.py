"""
进程间通信之共享内存
"""
from multiprocessing import Process
from multiprocessing import Value
from multiprocessing import Array
import ctypes

# 在共享内存中创建一个表示数值的ctypes对象
num1 = Value('d', 2.3)
num2 = Value(ctypes.c_float, 2.4)

# 在共享内存中创建一个表示数组的ctypes对象
arr1 = Array('i', range(1, 5))
arr2 = Array(ctypes.c_int, range(6, 10))


def do_sth():
    num1.value = 1.8
    num2.value = 2.4
    for i in range(len(arr1)):
        arr1[i] = -arr1[i]
    for i in range(len(arr2)):
        arr2[i] = -arr2[i]


p = Process(target=do_sth)
p.start()
p.join()

print(num1.value)
print(num2.value)
print(arr1[:])
print(arr2[:])

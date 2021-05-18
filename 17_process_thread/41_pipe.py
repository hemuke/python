from multiprocessing import Pipe

# 双工
conn1, conn2 = Pipe()

conn1.send('conn1第1次发送的数据')
conn1.send('conn1第2次发送的数据')

conn2.send('conn2第1次发送的数据')
conn2.send('conn2第2次发送的数据')

print(conn1.recv())
print(conn1.recv())

print(conn2.recv())
print(conn2.recv())


# 单工
c1, c2 = Pipe(False)

c2.send('c2发送的数据')
print(c1.recv())

# c1.send('c1发送的数据')

#网络传输只认字节，因此要进行编码

#a: str = "你好!"
#b: bytes = a.encode('gbk')
#print(b)
#c: str = b.decode('gbk')
#print(c)

import pickle

lst = ['成龙', '赵本山', '范伟']
#列表在内存里面的样子直接存储到硬盘上面去，将数据序列化

by = pickle.dumps(lst)
#转化成二进制的字节
print(by)

eby = pickle.loads(by)
print(eby)
# 转换成列表

#[不推荐]
dic = {'name':'admin', 'password':123}
f = open('data.txt', mode='w', encoding="utf-8")
f.write(str(dic))

f = open('data.txt', mode='r', encoding='utf-8')
s = f.read()
print(s)
print(type(s))
d = eval(s)    # eval对安全有影响
print(d, type(d))

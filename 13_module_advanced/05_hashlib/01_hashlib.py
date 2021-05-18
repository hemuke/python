import hashlib

# 创建md5对象
obj = hashlib.md5()

obj.update("666666".encode("utf-8"))

mi = obj.hexdigest()
print(mi)
# 撞库分析
# 6666,md5
# 7777,md5
# 正常的默认加密过程是容易撞库的问题
# 解决撞库: 加盐

obj = hashlib.md5(b'asdasdsdsadsa')
obj.update("666666".encode("utf-8"))
mi = obj.hexdigest()
print(mi)

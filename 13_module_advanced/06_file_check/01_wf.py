import hashlib

obj = hashlib.md5(b"abcdefg")

f = open('wf.txt', mode="rb")
for line in f:
    obj.update(line)

print(obj.hexdigest())

# 判断文件一致性
# 在我们上传文件的时候，首先计算机要上传的文件的md5，拿着这个值去网盘的数据库中
# 搜素有没有相同的md5。如果有，直接就是已经上传过，已经保存起来了

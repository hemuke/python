# 用户注册
import hashlib

def func(salt, password):
    obj = hashlib.md5(salt)
    obj.update(password.encode("utf-8"))
    return obj.hexdigest()

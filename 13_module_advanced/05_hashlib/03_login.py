import username_zhuce

username = input("用户名:")
f = open("user.txt", mode="r", encoding="utf-8")
password = username_zhuce.func(username.encode("utf-8"), password)
uname = f.readline().strip()
upwd = f.readline().strip()
if username == uname and password == upwd:
    print("登录成功")
else:
    print("登录失败")

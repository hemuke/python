import username_zhuce 

# 注册
username = input("请输入用户名:")
password = input("请输入密码:")
mi_password = username_zhuce.func(username.encode("utf-8"), password)

f = open('user.txt', mode='w', encoding='utf-8')
f.write(username)
f.write('\n')
f.write(mi_password)

# 登录
username = input("用户名:")
password = username_zhuce.func(username.encode("utf-8"), password)
f = open("user.txt", mode="r", encoding="utf-8")
uname = f.readline().strip()
upwd = f.readline().strip()
if username == uname and password == upwd:
    print("登录成功")
else:
    print("登录失败")

# 1）把python中的字典或者列表，转化为json字符串
# 2）前端返回的json字符串，转换为Python中的字典
import json
dic = {'id': 1, 'name':'我的天哪这么好玩', 'usertype': 0}
s = json.dumps(dic, ensure_ascii=False)
# s = json.dumps(dic) #json处理中文 不用ascii
print(s)
print(type(s))

s = '{"id":1, "name":"我的天哪这么好玩","usertype":0}'
d = json.loads(s)
print(d, type(d))

"""
前端的json和python中的字典有什么区别
d = {"id":1, "islogin": True, "hasGirl": None}
"""
d = {"id":1, "islogin": True, "hasGirl": None}
print(json.dumps(d))
# {"id": 1, "islogin": true, "hasGirl": null}

# 列表和字典都是OK
lst = ['A', 'B', 'C', 'D']
s = json.dumps(lst, ensure_ascii=False)
print(s, type(s))

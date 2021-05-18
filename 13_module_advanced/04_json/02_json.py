import json

wf = {
    "name":"汪峰",
    "age":18,
    "hobby":"上头条",
    "wife":{
        "name":'子怡',
        "age":19,
        "hobby":["唱歌", "跳舞", "演戏"]
    }
}

json.dump(wf, open("wf.txt", mode="w", encoding="utf-8"), ensure_ascii=False)

d = json.load(open("wf.txt", mode="r", encoding="utf-8"))
print(d, type(d))
print(d['wife']['name'])
print(d['wife']['hobby'][1])

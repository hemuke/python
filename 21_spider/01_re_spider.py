#! /root/anaconda3/bin/python
from urllib.request import Request
from urllib.request import urlopen
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def get_page(url):
    r = Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    })
    resp = urlopen(r)
    return resp.read().decode("utf-8")


def parse_page(s):
    obj = re.compile(
        r'<div class="item">.*?<em class="">(?P<rate>.*?)</em>.*?<span class="title">(?P<movie>.*?)</span>.*?<span class="rating_num" property="v:average">(?P<rating_num>.*?)</span>.*?<span>(?P<person_num>.*?)人评价</span>', re.S)
    res = obj.finditer(s)
    lst = []
    for item in res:
        dic = item.groupdict()
        lst.append(dic)
    return lst


def main():
    with open("movie.txt", mode="w", encoding="utf-8") as f:
        for i in range(10):
            s = get_page(f"https://movie.douban.com/top250?start={i * 25}&filter=")
            result = parse_page(s)
            for d in result:
                f.write(str(d))
                f.write("\n")


main()
